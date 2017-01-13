#!python3
#encoding:utf-8

import requests
import json
from datetime import datetime

class Auth:
    def __init__(self):
        pass

    def gets(self, username, password, otp=None):
        url = 'https://api.github.com/authorizations'
        headers = self._get_http_headers(otp)
        r = requests.get(url, headers=headers, auth=(username, password))
        with open('GiHubApi.Authorizations.List.{0}.json'.format(username), 'w') as f:
            f.write(r.text)
            print(r.text)

    def create(self, username, password, otp=None, scopes=None, note=None):
        if not(self.is_valid_grants(scopes)):
            raise Exception("invalid grant name. use from the following. : {0}".format(self.get_grants()))
        if (note is None):
            note = "token_note_{0:%Y%m%d%H%M%S%f}".format(datetime.now())
        data = {"scopes": scopes, "note": note}

        url = 'https://api.github.com/authorizations'
        headers = self._get_http_headers(otp)
        r = requests.post(url, headers=headers, auth=(username, password), data=json.dumps(data))
        print(r.text)
        res = json.loads(r.text)
        with open('GiHubApi.Authorizations.Create.{0}.{1}.json'.format(username, res['id']), 'w') as f:
            f.write(r.text)
            print(r.text)
        return res

    def _get_http_headers(self, otp):
        if (otp is None):
            headers = {'Time-Zone': 'Asia/Tokyo'}
        else:
            headers = {'Time-Zone': 'Asia/Tokyo', 'X-GitHub-OTP': otp}
        print(headers)
        return headers

    def get_grants(self):
        return ['repo', 'repo:status', 'repo_deployment', 'public_repo', 'admin:org', 'write:org', 'read:org', 'admin:public_key', 'write:public_key', 'read:public_key', 'admin:repo_hook', 'write:repo_hook', 'read:repo_hook', 'admin:org_hook', 'gist', 'notifications', 'user', 'user:email', 'user:follow', 'delete_repo', 'admin:gpg_key', 'write:gpg_key', 'read:gpg_key']

    def is_valid_grants(self, grants):
        for actual in grants:
            is_valid = False
            for expect in self.get_grants():
                if actual == expect:
                    is_valid = True
                    break
            if not(is_valid):
                print('invalid grant name: %s'.format(actual))
                return False
        return True
