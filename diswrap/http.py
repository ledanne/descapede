import aiohttp, json

ENDPOINT = "https://discord.com/api/v9/"

class Route:
    def __init__(self, method, url):
        self.method = method
        self.url = ENDPOINT + url

class HTTPClient:
    def __init__(self, token:str):
        self.client_session = None

        self.authentication = {
            "Authorization":f"Bot {token}",
            "Content-Type":"application/json"
        }
    
    async def connect(self, route:Route, payload:dict = {}):
        self.client_session = aiohttp.ClientSession()
        async with self.client_session as session:
            async with session.request(route.method, route.url, json = payload if payload else None, headers=self.authentication) as response:
                await self.close_session()
                
                return await response.json()
    
    async def login(self) -> bool:
        """
        Loginto discord bot. Returns True on success.
        """

        response = await self.connect(Route("GET", "users/@me"))

        if response.status == 200:
            return True
        else:
            return False
    
    async def close_session(self):
        await self.client_session.close()