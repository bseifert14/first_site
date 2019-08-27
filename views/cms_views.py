import flask
import services.cms_service as cms
from infrastructure.view_modifiers import response

blueprint = flask.Blueprint('cms', __name__, template_folder='templates')

@blueprint.route('/<path:full_url>')
@response(template_file='cms/page.html')
def cms_page(full_url: str):
    #LOGGER
    print('Getting CMS page for {}'.format(full_url))

    page = cms.get_page(full_url)
    if not page:
        return flask.abort(404)

    return page
