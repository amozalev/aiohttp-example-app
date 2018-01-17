from aiohttp import web, WSMsgType
import aiohttp_jinja2


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
            _ws.send_str('%s joined' % 'some_user')
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
            await _ws.send_str('%s disconnected' % 'some_user')
        return ws

# class WebSocket(web.View):
#     async def get(self):
#         ws = web.WebSocketResponse()
#         await ws.prepare(self.request)

# session = await get_session(self.request)
# user = User(self.request.db, {'id': session.get('user')})
# login = await user.get_login()
#
# for _ws in self.request.app['websockets']:
#     _ws.send_str('%s joined' % login)
# self.request.app['websockets'].append(ws)

# async for msg in ws:
#     if msg.tp == MsgType.text:
#         if msg.data == 'close':
#             await ws.close()
#         else:
#             message = Message(self.request.db)
#             result = await message.save(user=login, msg=msg.data)
#             log.debug(result)
#             for _ws in self.request.app['websockets']:
#                 _ws.send_str('(%s) %s' % (login, msg.data))
#     elif msg.tp == MsgType.error:
#         log.debug('ws connection closed with exception %s' % ws.exception())
#
# self.request.app['websockets'].remove(ws)
# for _ws in self.request.app['websockets']:
#     _ws.send_str('%s disconected' % login)
# log.debug('websocket connection closed')
#
# return ws
