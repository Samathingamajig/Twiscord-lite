import os # for importing environment variables for the bots to use
from twitchio.ext import commands as twitch_commands # Import the commands extension; also has the Bot subclass

class TwitchBot(twitch_commands.Bot):
  def __init__(self):
    # This initializing method is run when the bot is instantiated
    irc_token = os.environ['TWITCH_TMI_TOKEN']
    self.client_id = os.environ['TWITCH_CLIENT_ID']
    nick = os.environ['TWITCH_BOT_NICK'].lower()
    prefix = os.environ['TWITCH_BOT_PREFIX']
    self.initial_channel = os.environ['TWITCH_CHANNEL'].lower()
    self.twitch_link = f"https://twitch.tv/{self.initial_channel}"
    self._is_ready_ = False
    self.should_print = os.environ['PRINT_MESSAGES_TO_CONSOLE'].lower() in ("yes", "true", "t", "1")
    
    super().__init__(irc_token=irc_token, client_id=self.client_id, nick=nick, prefix=prefix, initial_channels=[f"#{self.initial_channel}"])  # For some reason, twitch wants a `#` at the beginning of the channel name
  
  async def event_ready(self):
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
    
    if not self.discord_bot._is_ready_:
      print("[Twiscord] Discord not initialized.")
      await message.channel.send("[Twiscord] Discord not initialized.")
      return
    
    sender_name = message.author.tags['display-name'] if 'display-name' in message.author.tags.keys() else message.author.name # Have to format with capitalization if it exists
    
    # Find the most relevant role for the chatter
    role = None
    if message.author.name == self.initial_channel:
      role = "Streamer"
    elif message.author.is_mod:
      role = "Moderator"
    elif message.author.is_subscriber:
      role = "Subscriber"
    
    content = f"{'**' + role + '** ' if role else ''}{sender_name} » {message.content}"
    if self.should_print: print(f"[twitch ] {content}")
    
    if message.startswith(self.prefix):
      # Have to call self.handle_commands since this is class-based
      await self.handle_commands(message)
    else:
      # Only send to the discord channel if it's not a command
      await self.discord_bot.channel.send(content)
    
  
  @twitch_commands.command(name="discord")
  async def discord(self, ctx):
    # If people type PREFIXdiscord, then reply with the discord server invite link
    # For example, if the prefix was '!', then !discord would run this
    await ctx.send(self.discord_bot.invite_link)

if __name__ == "__main__":
  # This file shouldn't be run, this is just the class extender
  # ./main.py is the file that should be ran
  print("Sorry, this isn't the file you meant to run.")
  print("You need to run for Twiscord to work ./main.py")