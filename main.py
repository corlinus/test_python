#!env python3

import sys
import signal
import websockets
import asyncio
import json

ws_list = {}

def signal_handler(sig, frame):
    print('\nExiting...')
    sys.exit(0)

def parse_messge(message):
    return json.loads(message)

def message_text(msg):
    return parse_messge(msg)['msg']

async def send_all(message):
    for ws, client_name in ws_list.items():
        await ws.send(message)

async def websocket_handler(websocket, path):
    await websocket.send('{"type":"auth_request"}')

    try:
        data = await websocket.recv()
    except websockets.exceptions.ConnectionClosed:
        websocket.close()
        return

    auth_message = parse_messge(data)
    name = auth_message['msg']

    global ws_list
    ws_list[websocket] = name
    print(f"`{name}` entered the chatroom.")
    await send_all('{\"type\":\"entered\",\"name\":\"%s\"}' % name)

    async for message in websocket:
        text = message_text(message)
        print(f"`{name}`: {text}")
        await send_all('{"type":"msg","name":"%s","text":"%s"}' % (name, text))

    await websocket.close()
    del ws_list[websocket]
    print(f"`{name}` left the chatroom.")
    await send_all('{"type":"left","name":"%s"}' % name)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C for exit')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(websockets.serve(websocket_handler, '127.0.0.1', 5000))
    loop.run_forever()

main()
