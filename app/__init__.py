from aiohttp import web
from .views import *
import jinja2
import aiohttp_jinja2

handler = Handler()


def init_app(argv):
    app = web.Application()
    app['ws_list'] = []
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./app/templates/'))

    app.router.add_static('/static', 'static', name='static')
    app.router.add_get('/', handler.hello)
    app.router.add_get('/ws', handler.websocket_handler)

    return app
