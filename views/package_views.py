import flask
import services.package_service as package_service
from infrastructure.view_modifiers import response

blueprint = flask.Blueprint('packages', __name__, template_folder='templates')

@blueprint.route('/project/<package_name>')
# @response(template_file='package/details.html')
def package_details(package_name: str):
    return "Package details for {}".format(package_name)


@blueprint.route('/<int:rank>')
def popular(rank: int):
    return "The details for the {}th most popular package".format(rank)
