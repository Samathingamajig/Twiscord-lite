import os # for importing environment variables for the bots to use
from twitchio.ext import commands as twitch_commands

class TwitchBot(twitch_commands.Bot):
  def __init__(self):
    irc_token = os.environ['TWITCH_TMI_TOKEN']
    client_id = os.environ['TWITCH_CLIENT_ID']
    nick = os.environ['TWITCH_BOT_NICK'].lower()
    prefix = os.environ['TWITCH_BOT_PREFIX']
    self.initial_channel = os.environ['TWITCH_CHANNEL'].lower()
    self._is_ready_ = False
    """
    Debug the variables
    """
    # print(irc_token)
    # print(client_id)
    # print(nick)
    # print(prefix)
    # print(self.initial_channels)
    # print()
    
    super().__init__(irc_token=irc_token, client_id=client_id, nick=nick, prefix=prefix, initial_channels=[f"#{self.initial_channel}"])  # For some reason, twitch wants a `#` at the beginning of the channel name
  
  async def event_ready(self):
    # import inspect
    # for name,thing in inspect.getmembers(self):
    #   print(name, ":", thing)
    print(f"Twitch Ready | {self.nick}") 
    self._is_ready_ = True
    self.channel = self.get_channel(self.initial_channel)
    if self.discord_bot._is_ready_:
      content = "[Twiscord] Discord and Twitch bots are set up."
      await self.channel.send(content)
      await self.discord_bot.channel.send(content)
      print(content)
  
  async def event_message(self, message):
    if message.author.name == self.nick.lower():
      return
    
    print("[twitch]", end=" ")
    if not self.discord_bot._is_ready_:
      print("[Twiscord] Discord not initialized.")
      await message.channel.send("[Twiscord] Discord not initialized.")
      return
    
    sender_name = message.author.tags['display-name'] if message.author.tags['display-name'] else message.author.name # Have to format with capitalization if it exists
    
    # Find the most relevant role for the chatter
    role = "Default"
    if message.author.name == self.initial_channel:
      role = "Streamer"
    elif message.author.is_mod:
      role = "Moderator"
    elif message.author.is_subscriber:
      role = "Subscriber"
    elif await self.get_follow(message.author.id, self.client_id):
      role = "Follower"
    
    content = f"**{role}** {sender_name} » {message.content}"
    print(content)
    await self.discord_bot.channel.send(content)
    