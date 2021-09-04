from .http import *
from .abc import User, Channel

class Client:
    """
    Base class for interacting with discord
    """

    def __init__(self, token: str):
        self.http = HTTPClient(token)
    
    async def myself(self) -> User:
        """
        Get the bot's userdata
        """

        response = await self.http.connect(Route("GET", "users/@me"))

        user = User()

        await user.from_dictionary(response)

        return user
    
    async def get_user(self, id:int) -> User:
        """
        Get userdata from ID
        """

        response = await self.http.connect(Route("GET", f"users/{id}"))

        user = User()

        await user.from_dictionary(response)

        return user
    
    async def get_channel(self, id: int):
        """
        Get a channel
        """

        response = await self.http.connect(Route("GET", f"channels/{id}"))

        channel = Channel()

        await channel.from_dictionary(response)

        channel.bot_caller = self
        
        return channel 

    async def close_connection(self):
        await self.http.close_session()