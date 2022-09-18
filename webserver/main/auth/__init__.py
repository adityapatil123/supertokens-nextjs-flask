from supertokens_python import init, InputAppInfo, SupertokensConfig
from supertokens_python.recipe.thirdpartyemailpassword import Google, Github, Apple
from supertokens_python.recipe import thirdpartyemailpassword, session

init(
    app_info=InputAppInfo(
        app_name="supertokens-with-next-js",
        api_domain="http://localhost:9000",
        website_domain="http://localhost:3000",
        api_base_path="/api/auth",
        website_base_path="/auth"
    ),
    supertokens_config=SupertokensConfig(
        connection_uri='http://localhost:3567',
        # api_key='someKey'
    ),
    framework='flask',
    recipe_list=[
        session.init(), # initializes session features
        thirdpartyemailpassword.init(
            providers=[
                # We have provided you with development keys which you can use for testing.
                # IMPORTANT: Please replace them with your own OAuth keys for production use.
                Google(
                    client_id='1060725074195-kmeum4crr01uirfl2op9kd5acmi9jutn.apps.googleusercontent.com',
                    client_secret='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'
                )
            ]
        )
    ]
)
