from .abc import Channel
from .http import Route

class DMChannel(Channel):
    recipient_id:int

    async def create_dm(self):
        response = await self.bot_caller.http.connect(Route("POST", f"users/@me/channels"), {
            "recipient_id":self.recipient_id
        })

        return response

    async def message(self, msg:str):
        response = await self.bot_caller.http.connect(Route("POST", f"channels/@me/{self.id}/messages"), {
            "content":msg
        })

        return response