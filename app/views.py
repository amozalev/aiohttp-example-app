from aiohttp import web, WSMsgType
import aiohttp_jinja2
import json
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

        # players_num = request.app['players_num']

        for _ws in request.app['ws_list']:
            request.app['players_num'] = request.app['players_num'] + 1
            msg = '%s joined' % 'some_user'
            json_data = {"message": str(msg), "players_num": request.app['players_num']}
            await _ws.send_json(json_data, dumps=json.dumps)
        request.app['ws_list'].append(ws)

        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                if msg.data == 'close':
                    print('close')
                    await ws.close()

                else:
                    for _ws in request.app['ws_list']:
                        json_data = {"message": str(msg.data), "players_num": request.app['players_num']}
                        await _ws.send_json(json_data, dumps=json.dumps)
            elif msg.type == WSMsgType.ERROR:
                print('ws connection closed with exception %s' % ws.exception())

        print('websocket connection closed')
        request.app['ws_list'].remove(ws)
        for _ws in request.app['ws_list']:
            request.app['players_num'] = request.app['players_num'] - 1
            msg = '%s disconnected' % 'some_user'
            json_data = {"message": str(msg), "players_num": request.app['players_num']}
            await _ws.send_json(json_data, dumps=json.dumps)
        return ws
