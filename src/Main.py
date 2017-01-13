#!python3
#encoding:utf-8
import dataset
import json
from github import Auth
from github import InsertAuth
from tkinter import Tk

db_path = 'C:/GitHub.Accounts.sqlite3'
username = 'github_username'
scopes = ['repo','delete_repo','gist']
note = 'test auth api.'

# DBからアカウント情報を取得する
db_connect_str = 'sqlite:///' + db_path
db = dataset.connect(db_connect_str)
account = db['Accounts'].find_one(Username = username)
two_factor = db['TwoFactors'].find_one(AccountId = account['Id'])

# GitHubAPIでAccessTokenを生成する
auth = Auth.Auth()
if (two_factor is None):
    res = auth.create(account['Username'], account['Password'], scopes=scopes, note=note)
else:
    otp = Tk().clipboard_get()
    res = auth.create(account['Username'], account['Password'], otp=otp, scopes=scopes, note=note)

# TokenをDBへ登録する
ins = InsertAuth.InsertAuth(db_path)
#ins.insert(account['Username'], json.loads(res))
ins.insert(account['Username'], res)
