import asyncio
import websockets


async def notificaciones(websocket, path):
    while True:
        # Espera mensajes desde el cliente (no es necesario para notificaciones unidireccionales)
        mensaje_del_cliente = await websocket.recv()
        print(f"Mensaje del cliente: {mensaje_del_cliente}")

        # Envía una notificación al cliente
        mensaje_notificacion = "¡Hola desde el servidor!"
        await websocket.send(mensaje_notificacion)
        await asyncio.sleep(5)  # Simula un intervalo de notificación


start_server = websockets.serve(notificaciones, "localhost", 5555)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
