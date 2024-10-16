import asyncio
import json

from websockets.asyncio.server import ServerConnection, serve


async def send_imgs(websocket: ServerConnection):
    while True:
        await websocket.send(
            json.dumps(
                [
                    {
                        "imgUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/%E6%9D%B1%E4%BA%AC%E3%82%BF%E3%83%AF%E3%83%BC_%28214699253%29.jpeg/640px-%E6%9D%B1%E4%BA%AC%E3%82%BF%E3%83%AF%E3%83%BC_%28214699253%29.jpeg",
                        "name": "東京タワー",
                        "yomigana": "とうきょうたわー",
                        "lon": 139.74556,
                        "lat": 35.65861,
                    }
                ]
            )
        )

        await asyncio.sleep(5)

        await websocket.send(
            json.dumps(
                [
                    {
                        "imgUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/%E6%9D%B1%E4%BA%AC%E3%82%BF%E3%83%AF%E3%83%BC_%28214699253%29.jpeg/640px-%E6%9D%B1%E4%BA%AC%E3%82%BF%E3%83%AF%E3%83%BC_%28214699253%29.jpeg",
                        "name": "東京タワー",
                        "yomigana": "とうきょうたわー",
                    },
                    {
                        "imgUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/%E3%82%B9%E3%82%AB%E3%82%A4%E3%83%84%E3%83%AA%E3%83%BC_-_panoramio_%2820%29.jpg/640px-%E3%82%B9%E3%82%AB%E3%82%A4%E3%83%84%E3%83%AA%E3%83%BC_-_panoramio_%2820%29.jpg",
                        "name": "東京スカイツリー",
                        "yomigana": "とうきょうすかいつりー",
                    },
                    {
                        "imgUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/%E9%9B%B7%E9%96%80%E3%80%82_-_panoramio.jpg/640px-%E9%9B%B7%E9%96%80%E3%80%82_-_panoramio.jpg",
                        "name": "雷門",
                        "yomigana": "かみなりもん",
                    },
                ]
            )
        )

        await asyncio.sleep(5)

        await websocket.send(
            json.dumps(
                [
                    {
                        "lon": 139.74556,
                        "lat": 35.65861,
                        "name": "東京タワー",
                        "yomigana": "とうきょうたわー",
                    },
                ]
            )
        )

        await asyncio.sleep(5)


async def main():
    async with serve(send_imgs, "localhost", 9999):
        await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())
