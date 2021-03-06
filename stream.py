# -*- coding: utf-8 -*-
import operator
from urllib.parse import urljoin

import requests


class MstdnStream:
    def __init__(self, base_url, access_token, listener):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({'Authorization': 'Bearer ' + access_token})
        self.listener = listener

    def public(self):
        url = urljoin(self.base_url, '/api/v1/streaming/public')
        resp = self.session.get(url, stream=True)
        resp.raise_for_status()
        event = {}
        for line in resp.iter_lines():
            line = line.decode('utf-8')

            if not line:
                # End of content.
                method_name = "on_{event}".format(event=event['event'])
                f = operator.methodcaller(method_name, event['data'])
                f(self.listener)
                # refreash
                event = {}
                continue

            if line.startswith(':'):
                # TODO: Handle heatbeat
                print('startwith ":" {line}'.format(line=line))
            else:
                key, value = line.split(': ', 1)
                if key in event:
                    event[key] += value
                else:
                    event[key] = value

    def _dispatch_event(self, event):
        method_name = "on_{event}".format(event=event['event'])
        f = operator.methodcaller(method_name, event['data'])
        f(self.listener)

    def _handle_heartbeat(self, line):
        # TODO: Handle heatbeat
        print(line)

    def _run(self, path, params=None):
        if params is None:
            params = {}
        url = urljoin(self.base_url, path)
        resp = self.session.get(url, params=params, stream=True)
        resp.raise_for_status()

        event = {}
        for line in resp.iter_lines():
            line = line.decode('utf-8')

            if not line:
                # End of content.
                self._dispatch_event(event)

                # Format dict
                event = {}
                continue

            if line.startswith(':'):
                self._handle_heartbeat(line)
            else:
                key, value = line.split(': ', 1)
                if key in event:
                    event[key] += value
                else:
                    event[key] = value

    def public(self):
        self._run('/api/v1/streaming/public')

    def local(self):
        self._run('/api/v1/streaming/public/local')

    def user(self):
        self._run('/api/v1/streaming/user')

    def hashtag(self, tag):
        self._run('/api/v1/streaming/hashtag', params={'tag': tag})

    def local_hashtag(self, tag):
        self._run('/api/v1/streaming/hashtag/local', params={'tag': tag})


class MstdnStreamListner:

    def on_update(self, data):
        print(data)

    def on_notification(self, data):
        print(data)

    def on_delete(self, data):
        print("Deleted: {id}".format(id=data))
