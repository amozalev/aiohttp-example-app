from aiohttp import web
import app
import config

app = app.init_app(argv=None)
web.run_app(app, port=config.PORT)

if __name__ == '__main__':
    web.run_app(app, port=config.PORT)
