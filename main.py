import asyncio # Required for running both bots at the same time

# Import both bot classes from twitch_bot.py and discord_bot.py
from twitch_bot import TwitchBot 
from discord_bot import DiscordBot

def main():
  # Instantiate each class
  twitch_bot = TwitchBot()
  discord_bot = DiscordBot()
  
  # Add a reference to the other bot to each bot
  twitch_bot.discord_bot = discord_bot
  discord_bot.twitch_bot = twitch_bot
  
  # This is used get both bots running at the same time
  # Using the normal bot.run() would be blocking, so only one bot could run at a time
  loop = asyncio.get_event_loop()
  task1 = loop.create_task(twitch_bot.start())
  task2 = loop.create_task(discord_bot.start())
  gathered = asyncio.gather(task1, task2, loop=loop)
  loop.run_until_complete(gathered)

if __name__ == "__main__":
  # Run the main function if this file is run
  # (if someone import this as a library, we don't want to run main immediately)
  main()