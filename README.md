# hacking example-oath2-server

学习example-oath2-server

# 部署步骤

```PowerShell
python3 -m venv venv
# PowerShell
.\venv\Scripts\activate

pip3 install -r .\requirements.txt

(venv) flask initdb
(venv) flask run
```

# 使用步骤

1. 访问`http://127.0.0.1:5000/`；
2. 使用用户名`Hi`登录，然后点击`create_client`链接进入`http://127.0.0.1:5000/create_client`创建一个client；
3. 填写以下字段

![create_cleint](https://user-images.githubusercontent.com/290496/38811988-081814d4-41c6-11e8-88e1-cb6c25a6f82e.png)

- Client Name: Hi
- Client URI: https://authlib.org/
- Allowed Scope: profile
- Redirect URIs: https://authlib.org/
- Allowed Grant Types: authorization_code password
- Allowed Response Types: code

4. 之后会响应一个json，使用工具发送POST请求获取access_token

响应：

```
{"client_id": <client_id>, "client_id_issued_at": 1525224625, "client_secret": <client_secret>, "client_secret_expires_at": 0}
{"client_name": "Hi", "client_uri": "https://authlib.org/", "contacts": [], "grant_types": ["authorization_code", "password"], "jwks": null, "jwks_uri": null, "logo_uri": null, "policy_uri": null, "redirect_uris": ["https://authlib.org/"], "response_types": ["code"], "
```

再请求

```
curl -u ${client_id}:${client_secret} -XPOST http://127.0.0.1:5000/oauth/token -F grant_type=password -F username=${username} -F password=valid
```

响应：

```
{
  "access_token": <access_token>
  "expires_in": 864000,
  "token_type": "Bearer"
}
```

5. 之后就可以拿这个`access token`向资源服务器获取资源；
6. 资源服务器使用令牌向认证服务器确认令牌的正确性，确认无误后提供资源。


