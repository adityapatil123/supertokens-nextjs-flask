import os

from main import create_app


app = create_app(os.getenv("ENV") or "dev")


if __name__ == "__main__":
    if os.getenv("ENV") is not None:
        # flask_s3.create_all(app)
        app.run(host="0.0.0.0", port=app.config["PORT"])

# import os
#
# from flask import Flask, abort, g, jsonify, make_response, request
# from flask_cors import CORS
# from supertokens_python import (
#     InputAppInfo,
#     SupertokensConfig,
#     get_all_cors_headers,
#     init,
# )
# from supertokens_python.framework.flask import Middleware
# from supertokens_python.recipe import session, thirdpartyemailpassword
# from supertokens_python.recipe.session.framework.flask import verify_session
# from supertokens_python.recipe.session.syncio import refresh_session
# from supertokens_python.recipe.thirdpartyemailpassword import Google
#
#
# def get_api_port():
#     return "3001"
#
#
# def get_website_port():
#     return "3000"
#
#
# def get_website_domain():
#     return "http://localhost:" + get_website_port()
#
#
# init(
#     supertokens_config=SupertokensConfig(connection_uri="http://localhost:3567"),
#     app_info=InputAppInfo(
#         app_name="supertokens-with-next-js",
#         api_domain="http://localhost:9000",
#         website_domain="http://localhost:3000",
#         api_base_path="/api/auth",
#         website_base_path="/auth"
#     ),
#     framework="flask",
#     recipe_list=[
#         session.init(),
#         thirdpartyemailpassword.init(
#             providers=[
#                 Google(
#                     client_id='1060725074195-kmeum4crr01uirfl2op9kd5acmi9jutn.apps.googleusercontent.com',
#                     client_secret='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'
#                 )
#             ]
#         ),
#     ],
#     telemetry=False,
# )
#
# app = Flask(__name__)
# Middleware(app)
# CORS(
#     app=app,
#     supports_credentials=True,
#     origins=get_website_domain(),
#     allow_headers=["Content-Type"] + get_all_cors_headers(),
# )
#
# # @app.route("/api/auth/session/refresh", methods=["POST"])  # type: ignore
# # def custom_refresh():  # type: ignore
# #     response = make_response(jsonify({}))
# #     refresh_session(request)
# #     return response
#
#
# @app.route("/sessioninfo", methods=["GET"])  # type: ignore
# @verify_session()
# def get_session_info():
#     session_ = g.supertokens
#     return jsonify(
#         {
#             "sessionHandle": session_.get_handle(),
#             "userId": session_.get_user_id(),
#             "accessTokenPayload": session_.get_access_token_payload(),
#         }
#     )
#
#
# # This is required since if this is not there, then OPTIONS requests for
# # the APIs exposed by the supertokens' Middleware will return a 404
# @app.route("/", defaults={"u_path": ""})  # type: ignore
# @app.route("/<path:u_path>")  # type: ignore
# def catch_all(u_path: str):  # pylint: disable=unused-argument
#     abort(404)
#
#
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=9000, debug=True)
