#!python3
#encoding:utf-8
import dataset
class InsertAuth:
    def __init__(self, db_path):
        self.db_path = db_path
        db_connect_str = 'sqlite:///C:/root/db/Account/GitHub/private/GitHub.Accounts.sqlite3'
        db_connect_str = 'sqlite:///' + db_path
        self.db = dataset.connect(db_connect_str)

    """
    Insert the results of the Auth API into the Database.
    @param [String] username is github username.
    @param [String] res is [Create a new authorization](https://developer.github.com/v3/oauth_authorizations/#create-a-new-authorization) API response.
    """
    def insert(self, username, res):
        account = self.db['Accounts'].find_one(Username=username)
        account['Id']
#        self.db['AccessTokens'].insert(dict(AccountId=account['Id'], IdOnGitHub=res['id'], Note=res['note'], AccessToken=res['token'], Scopes=res['scopes']))
        print('res.scopes = {0}'.format(res['scopes']))
#        print('map(str, res.scopes) = {0}'.format(map(str,res['scopes'])))
        print('\".\".join(map(str, res.scopes)) = {0}'.format(",".join(map(str,res['scopes']))))

        self.db['AccessTokens'].insert(dict(AccountId=account['Id'], IdOnGitHub=res['id'], Note=res['note'], AccessToken=res['token'], Scopes=",".join(map(str,res['scopes']))))
        
        for token in self.db['AccessTokens']:
            print(token)
