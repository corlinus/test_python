#!env python3

import sys
import signal
import websockets
import asyncio

ws_list = {}

def signal_handler(sig, frame):
    print('\nExiting...')
    sys.exit(0)

async def send_all(message):
    for ws, client_name in ws_list.items():
        await ws.send(message)

async def websocket_hadler(websocket, path):
    await websocket.send("Say your name!")
    auth_message = await websocket.recv()
    name = auth_message

    global ws_list
    ws_list[websocket] = name
    enter_message = f"`{name}` entered the chatroom."
    print(enter_message)
    await send_all(enter_message)

    async for message in websocket:
        msg_text = f"{name}: {message}"
        print(msg_text)
        await send_all(msg_text)

    await websocket.close()
    del ws_list[websocket]
    left_message = f"`{name}` left the chatroom."
    print(left_message)
    await send_all(left_message)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C for exit')

    loop = asyncio.get_event_loop()
    loop.run_until_complete(websockets.serve(websocket_hadler, '127.0.0.1', 5000))
    loop.run_forever()

main()
