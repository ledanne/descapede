from .http import *

class Client:
    """
    Base class for interacting with discord
    """

    def __init__(self, token: str):
        self.http = HTTPClient(token)
    
    async def myself(self):
        """
        Get the bot's userdata
        """

        response = await self.http.connect(Route("GET", "users/@me"))

        if response.status == 200:
            response_json = "something"
            return response_json

    async def close_connection(self):
        await self.http.close_session()