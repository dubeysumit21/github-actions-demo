import asyncio
import time
from ably import AblyRealtime

API_KEY = "dluB1w.ls-ILA:HZBxKXk8YJ_fbdKOgK9HX5z6_T8tMmLHj71_fQv-Zvg"
CHANNEL = "gh-actions-logs"


async def main():
    client = AblyRealtime(API_KEY)
    channel = client.channels.get(CHANNEL)

    async def on_message(msg):
        print(f"{time.strftime('%H:%M:%S')}  {msg.data}")

    await channel.subscribe("log", on_message)
    print(f"Listening on '{CHANNEL}'... (Ctrl+C to stop)")
    await asyncio.Event().wait()


asyncio.run(main())
