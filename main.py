import asyncio # Required for running both bots
from twitch_bot import TwitchBot
from discord_bot import DiscordBot

def main():
  twitch_bot = TwitchBot()
  discord_bot = DiscordBot()
  
  twitch_bot.discord_bot = discord_bot
  discord_bot.twitch_bot = twitch_bot
  
  loop = asyncio.get_event_loop()
  task1 = loop.create_task(twitch_bot.start())
  task2 = loop.create_task(discord_bot.start())
  gathered = asyncio.gather(task1, task2, loop=loop)
  loop.run_until_complete(gathered)

if __name__ == "__main__":
  main()