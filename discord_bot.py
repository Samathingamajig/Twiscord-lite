import os # for importing environment variables for the bots to use
import discord
from discord.ext import commands as discord_commands, tasks

class DiscordBot(discord_commands.Bot):
  def __init__(self):
    self.token = os.environ['DISCORD_TOKEN']
    self.channel_id = int(os.environ['DISCORD_CHANNEL_ID'])
    self.channel = None # Will be set later
    self.invite_link = os.environ['DISCORD_INVITE_LINK']
    print("Discord __init__")
    self._is_ready_ = False
    
    command_prefix = os.environ['DISCORD_BOT_PREFIX']
    
    super().__init__(command_prefix=command_prefix)
    
  def start(self):
    # This function overrides the default `start` function
    # since I want to be able to just call `start` from
    # `main.py` and configure the token from here
    print("Discord start")
    return super().start(self.token)
  
  async def on_ready(self):
    print(f"Discord Ready | {self.user}")
    self.channel = self.get_channel(self.channel_id)
    self._is_ready_ = True
    if self.twitch_bot._is_ready_:
      content = "[Twiscord] Discord and Twitch bots are set up."
      await self.channel.send(content)
      await self.twitch_bot.channel.send(content)
      print(content)
  
  async def on_message(self, message):
    if message.author == self.user:
      return # Don't respond to messages from yourself
    
    if not self.twitch_bot._is_ready_: # Make sure that the twitch bot is up and running
      await message.channel.send("[Twiscord] Twitch not initialized.")
      print("[Twiscord] Twitch not initialized.")
      return
    
    
    
    if message.channel.id == self.channel_id:
      print("[discord]", end=" ")
      content = f"{'[' + str(message.author.top_role) + '] ' if message.author.top_role else ''}{message.author} » {message.clean_content}"[:300] # Only take the first 300 characters, 500 is officially the max but 300 should be all you need
      print(content)
      if message.clean_content.startswith(self.command_prefix): await self.handle_commands(message)
      else: await self.twitch_bot.channel.send(content)
      
    else:
      return # Wrong channel
  
  async def handle_commands(self, message):
    content = message.clean_content[len(self.command_prefix):]
    if content.startswith('twitch'):
      await self.twitch(message)
  
  async def twitch(self, message):
    await message.channel.send(self.twitch_bot.twitch_link)

if __name__ == "__main__":
  print("Sorry, this isn't the file you meant to run.")
  print("You need to run for Twiscord to work ./main.py")