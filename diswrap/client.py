from .http import *
from .abc import User, Channel
from .channels import DMChannel

import asyncio as aio

class Client:
    """
    Base class for interacting with discord
    """

    def __init__(self, token: str):
        self.http = HTTPClient(token)

        self.event_loop = aio.new_event_loop()
        aio.set_event_loop(self.event_loop)

        self.events = {
            "ready":None,
            "tick":None
        }
    
    def event(self, _coro):
        """
        Override event

        =====

        event_name: can be 'ready' to initiate on login
        """

        self.events[_coro.__name__] = _coro

        return _coro
    
    async def login(self) -> User:
        """
        Get the bot's userdata
        """

        response = await self.http.connect(Route("GET", "users/@me"))

        if self.events["ready"]:
            await self.events["ready"]()

        user = User()

        await user.from_dictionary(response)

        return user
    
    async def run(self):
        await self.login()

        while True:
            await aio.sleep(0.05)

            await self.events["tick"]()
    
    async def send_typing(self, channel:Channel):
        response = await self.http.connect(Route("POST", f"channels/{channel.id}/typing"))

        return response
    
    async def get_user(self, id:int) -> User:
        """
        Get userdata from ID
        """

        response = await self.http.connect(Route("GET", f"users/{id}"))

        user = User()

        await user.from_dictionary(response)

        return user
    
    async def get_channel(self, id: int, dm:bool=False):
        """
        Get a channel
        """

        url = f"channels/@me/{id}" if dm else f"channels/{id}"

        response = await self.http.connect(Route("GET", url))

        channel = Channel() if not dm else DMChannel()

        await channel.from_dictionary(response)

        channel.bot_caller = self
        
        return channel 

    async def close_connection(self):
        await self.http.close_session()