from aiohttp import web
import config


def hello(request):
    return web.Response(text='Hello!')


def init_app(argv):
    app = web.Application()
    app.router.add_get('/', hello)
    web.run_app(app, port=config.PORT)


if __name__ == '__main__':
    init_app()
