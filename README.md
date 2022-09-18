# supertokens-nextjs-flask
Authentication setup using Supertokens with next-js(frontend) and flask(backend)

## Frontend
1. Run react development server
```
npm install
npm dev run
```
2. Open http://localhost:3000 to confirm the success
3. Open http://localhost:3000/auth for Supertokens auth page

## Backend
1. Run flask server (with [restx](https://flask-restx.readthedocs.io/en/latest/))
```
pip3 install requirements.txt
EXPORT ENV=dev
python3 -m manage.py
```
2. Open http://localhost:9000/search to confirm the success

## Supertokens Core
1. Run Supertokens using docker
```
docker run -p 3567:3567 -d registry.supertokens.io/supertokens/supertokens-postgresql
```
2. Open http://localhost:3567/hello to confirm the success


## Points to be remember:
1. Backend configuration for supertokens
```
app_name="supertokens-with-next-js",
api_domain="http://localhost:9000",  // Backend service endpoint
website_domain="http://localhost:3000", // Frontend service endpoint
api_base_path="/api/auth",
website_base_path="/auth"

connection_uri='http://localhost:3567'  // Supertokens Core service endpoint
```
2. Update recipe list: [(Link)](https://supertokens.com/docs/thirdpartyemailpassword/quick-setup/frontend)
```
ThirdPartyEmailPassword.init({
    signInAndUpFeature: {
        providers: [
            Github.init(),
            Google.init(),
            Facebook.init(),
            Apple.init(),
        ]
    }
}),
Session.init()
```
3. Secured website route `/posts/first-post` [(Link)](https://supertokens.com/docs/thirdpartyemailpassword/common-customizations/sessions/securing-component)
4. Secured api route `/protected-search` [(Link)](https://supertokens.com/docs/thirdpartyemailpassword/common-customizations/verify-session)
