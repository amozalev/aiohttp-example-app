from aiohttp import web
from .views import *
import jinja2
import aiohttp_jinja2

handler = Handler()


def init_app(argv):
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('./app/templates/'))

    app.router.add_get('/', handler.hello)
    app.router.add_get('/game', handler.websocket_handler)

    return app
