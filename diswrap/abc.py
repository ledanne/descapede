from typing import (
    Union,
    Any
)

from .http import Route

class User:
    id: int
    username:int
    avatar:str
    discriminator:str
    public_flags:int
    flags:int
    bot:bool
    banner:str
    banner_color:Union[Any]
    accent_color:Union[Any]
    bio:str
    locale:str
    mfa_enabled:bool
    email:str
    verified:bool

    bot_caller:Union[Any]

    def mentionable(self) -> str:
        return f"<@{self.id}>"
    
    async def from_dictionary(self, dictionary:dict):
        for key in dictionary:
            setattr(self, key, dictionary[key])
    
    async def to_dictionary(self) -> dict:
        return self.__dict__

class Message:
    id:int
    type:int
    content:str
    channel_id:int
    author:User
    attachments:list
    embeds:list
    mentions:list
    mention_roles:[]
    pinned:bool
    mention_everyone:bool
    tts:bool
    timestamp:str
    edited_timestamp:str
    flags:int
    components:list

    async def from_dictionary(self, dictionary:dict):
        for key in dictionary:
            if key == "author":
                user = User()
                await user.from_dictionary(dictionary)

                self.author = user
            else:
                setattr(self, key, dictionary[key])
    
    async def to_dictionary(self) -> dict:
        return self.__dict__

class Channel:
    id:int
    last_message_id:int
    type:int
    name:str
    position:int
    parent_id:int
    topic:str
    guild_id:int
    permission_overwrites:list
    nsfw:bool
    rate_limit_per_user:int

    bot_caller:Union[Any]
    
    async def from_dictionary(self, dictionary:dict):
        for key in dictionary:
            setattr(self, key, dictionary[key])
    
    async def to_dictionary(self) -> dict:
        return self.__dict__
    
    async def last_message(self):
        response = await self.bot_caller.http.connect(Route("GET", f"channels/{self.id}/messages/{self.last_message_id}"))
        message = Message()

        await message.from_dictionary(response)
        return message
    
    async def message(self, message:str):
        response = await self.bot_caller.http.connect(Route("POST", f"channels/{self.id}/messages"), {
            "content":message,
            "tts":False,
            "nonce":None,
            "embeds":[],
            "sticker_ids":[],
            "components":[],
            "message_reference":None
        })

        return response
    
    def mentionable(self) -> str:

        return f"<#{self.id}>"