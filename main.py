from diswrap import Client
import aiohttp

import os
import asyncio

async def main():
    token = os.environ["token"]

    client = Client(token)

    user = await client.myself()

    print(user)
    
asyncio.run(main())