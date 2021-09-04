from diswrap import Client
import aiohttp

import os
import asyncio

async def main():
    token = os.environ["token"]

    client = Client(token)

    channel = await client.get_channel(870770512513630248)

    last_message = await channel.last_message()

    print(await last_message.to_dictionary())

    response = await channel.message("jhelo")

    print(response)
    
asyncio.run(main())