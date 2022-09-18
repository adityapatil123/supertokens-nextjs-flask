from flask import g, request
from flask_restx import Namespace, Resource
# from main.service.search import add_search_catalogues, get_catalogues_for_message_id, gateway_search
from supertokens_python.recipe.session.framework.flask import verify_session

search_namespace = Namespace('search', description='Search Namespace')


@search_namespace.route("/protected-search")
class ProtectedSearch(Resource):

    @verify_session()
    def get(self):
        return {"message": "Success!"}


@search_namespace.route("/search")
class Search(Resource):

    def get(self):
        return {"message": "Success!"}

