from aiohttp import web, WSMsgType
import aiohttp_jinja2
from . import models


class Handler:

    def __init__(self):
        pass

    @aiohttp_jinja2.template('index.html')
    def hello(self, request):
        # return web.Response(text='Hello!')
        return {'text': 'Hello!'}

    async def websocket_handler(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        for _ws in request.app['ws_list']:
            request.app['players_num'] = request.app['players_num'] + 1
            print(request.app['players_num'])
            message = '%s joined' % 'some_user'
            players_num = request.app['players_num']
            json_data = {'message': message, 'players_num': players_num}
            _ws.send_json(json_data)
        request.app['ws_list'].append(ws)

        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                if msg.data == 'close':
                    print('close')
                    await ws.close()

                else:
                    for _ws in request.app['ws_list']:
                        await _ws.send_str(msg.data)
            elif msg.type == WSMsgType.ERROR:
                print('ws connection closed with exception %s' % ws.exception())

        print('websocket connection closed')
        request.app['ws_list'].remove(ws)
        for _ws in request.app['ws_list']:
            request.app['players_num'] = request.app['players_num'] - 1
            msg = '%s disconnected' % 'some_user'
            await _ws.send_str(msg)
        return ws
