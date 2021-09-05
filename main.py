from diswrap import Client, DMChannel
import aiohttp

import os
import asyncio

token = os.environ["token"]
client = Client(token)

@client.event
async def ready():
    channel = await client.get_channel(860915745927331891)

    setattr(client, "mychannel", channel)

last_message = None

@client.event
async def tick():
    last_message = await client.mychannel.last_message()
    if last_message:
        message = await client.mychannel.last_message()

        if last_message != message:
            if message.content == "do shit my bot":
                await client.mychannel.message("ok bitch")
            
            last_message = message

asyncio.run(client.run())