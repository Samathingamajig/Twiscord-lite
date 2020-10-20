import os # for importing environment variables for the bots to use
import discord
from discord.ext import commands as discord_commands

class DiscordBot(discord_commands.Bot):
  def __init__(self):
    self.token = os.environ['DISCORD_TOKEN']
    self.channel_id = int(os.environ['DISCORD_CHANNEL_ID'])
    self.channel = None # Will be set later
    self.invite_link = os.environ['DISCORD_INVITE_LINK']
    self._is_ready_ = False
    self.should_print = os.environ['PRINT_MESSAGES_TO_CONSOLE'].lower() in ("yes", "true", "t", "1")
    
    command_prefix = os.environ['DISCORD_BOT_PREFIX']
    
    super().__init__(command_prefix=command_prefix)
    
  def start(self):
    # This function overrides the default `start` function
    # since I want to be able to just call `start` from
    # `main.py` and configure the token from here.
    # This returns the co-routine of the bot, needed for running both bots at once.
    return super().start(self.token)
  
  async def on_ready(self):
    print(f"Discord Ready | {self.user}")
    self.channel = self.get_channel(self.channel_id)
    self._is_ready_ = True
    if self.twitch_bot._is_ready_: # If both bots are ready/set up, send message to discord and twitch channel
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
      content = f"{'[' + str(message.author.top_role) + '] ' if message.author.top_role else ''}{message.author} » {message.clean_content}"[:300] # Only take the first 300 characters, 500 is officially the max but 300 should be all you need
      if self.should_print: print(f"[discord] {content}")
      if message.clean_content.startswith(self.command_prefix): await self.handle_commands(message) # If the message starts with the prefix, then send the message to self.handle_commands 
      else: await self.twitch_bot.channel.send(content) # If it's not a command, then send the message to the twitch chat
      
    else:
      return # Wrong channel
  
  async def handle_commands(self, message):
    """
    Class based discord.ext.commands.Bot extenders don't have
    a simple way to handle functional based commands.
    
    If you're making a discord bot that is class based like this,
    then I'd recommend using this.
    """
    command = message.clean_content[len(self.command_prefix):].split(" ")[0] # Get the first word after the prefix
    arguments = message.clean_content[len(self.command_prefix):].split(" ")[1:] # Get a list of all the arguments after the prefix and after the command keyword
    
    if command == 'twitch':
      await self.twitch(message, arguments)
  
  async def twitch(self, message, arguments):
    # If people type PREFIXtwitch, then reply with the twitch channel link
    # For example, if the prefix was '!', then !twitch would run this
    await message.channel.send(self.twitch_bot.twitch_link)

if __name__ == "__main__":
  # This file shouldn't be run, this is just the class extender
  # ./main.py is the file that should be ran
  print("Sorry, this isn't the file you meant to run.")
  print("You need to run for Twiscord to work ./main.py")