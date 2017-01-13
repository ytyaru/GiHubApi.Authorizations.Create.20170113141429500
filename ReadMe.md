# このソフトウェアについて

GiHubApi.Authorizations.Create.20170113141429500は私個人が学習目的で作成したソフトウェアである。
GitHubのAccessTokenを作成するAPIを実行してDBに挿入する。

# 開発環境

* Windows XP Pro SP3 32bit
    * cmd.exe
* [Python 3.4.4](https://www.python.org/downloads/release/python-344/)
    * [requests](http://requests-docs-ja.readthedocs.io/en/latest/)
    * [dataset](https://github.com/pudo/dataset)
* [WinAuth](https://winauth.com/download/)

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 準備

* [GitHubアカウント](https://github.com/join?source=header-home)を作成する
* [AccessToken](https://github.com/settings/tokens)を1つ以上作成する
* [GitHub.Accounts.Database](https://github.com/ytyaru/GitHub.Accounts.Database.20170107081237765)でGitHubアカウントDBを作成する
* Main.pyでGitHubのusernameを指定する
* Main.pyでSQLiteのDBファイルパスを指定する
* Main.pyでscopesを設定する
* Main.pyでnoteを設定する

TwoFactor認証アカウントを使う場合、WinAuthで取得できるようにしておく。

* [Two-Factor認証を有効にする設定](https://github.com/settings/two_factor_authentication/intro)を行う
* [WinAuth](https://winauth.com/download/)などでOTP(One-Time-Password)を取得する

# 実行

```dosbatch
python Main.py
```

TwoFactor認証アカウントを使う場合、WinAuthで取得してから実行すると、クリップボードからOTPを取得してAPIを実行する。

WinAuthでOTPを取得してから変更されるまでの間(30秒間)に、`Main.py`を実行すること。

# 結果

[Create a new authorization API](https://developer.github.com/v3/oauth_authorizations/#create-a-new-authorization)の結果が`GiHubApi.Authorizations.Create.{username}.{id}.json`ファイルに出力される。また、DBに登録される。

## note重複エラー

noteが重複すると以下のようなエラーになる。Tokenを削除するか、重複しない別の名前にすること。

```json
{"message":"Validation Failed","errors":[{"resource":"OauthAccess","code":"already_exists","field":"description"}],"documentation_url":"https://developer.github.com/v3/oauth_authorizations/#create-a-new-authorization"}
```

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
