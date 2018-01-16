from aiohttp import web, WSMsgType
import aiohttp_jinja2


class Handler:
    def __init__(self):
        pass

    @aiohttp_jinja2.template('index.html')
    def hello(self, request):
        # return web.Response(text='Hello!')
        return {'text': 'Hello!'}

    async def websocket_handler(request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                if msg.data == 'close':
                    await ws.close()
                else:
                    await ws.send_str(msg.data + '/answer')
            elif msg.type == WSMsgType.ERROR:
                print('ws connection closed with exception %s' %
                      ws.exception())
        print('websocket connection closed')
        return ws