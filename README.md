![Twiscord](https://raw.githubusercontent.com/Samathingamajig/Twiscord/master/twiscord-big-logo.png)
# Twiscord: Sync Twitch and Discord chat with Python

## What is Twiscord?
Twiscord syncs your Twitch channel's chat with a Discord channel's chat, both ways. This is simple to do unidirectional with webhooks, but for bidirectional this is a challenge. That's why [Samathingamajig](https://github.com/Samathingamajig) created this app, to make this process simple.

## What is Twiscord build upon?
Twiscord is directly built upon 3 libraries:
+ [Discord.py](https://github.com/Rapptz/discord.py) » For the Discord bot portion
+ [Twitchio](https://github.com/TwitchIO/TwitchIO) » For the Twitch bot portion
+ [asyncio](https://docs.python.org/3/library/asyncio.html) » Required for running both bots at the same time

## How do I install this?
> How to install on Windows:
1. Run this: `py -3 -m pip install pipenv` to install pipenv. This is how the `.env` file use utilized.

2. Go to Settings » System » About (left) » System info (top right) » Advanced system settings (left) » Enviornment Variables ... » Path » Edit » Add this: `C:\Users\YOURUSERNAMEGOESHERE\AppData\Roaming\Python\Python38\Scripts` (make sure to change the username). This lets `pipenv` run as a global script.

3. (Assuming you have installed Git) Run this: `https://github.com/Samathingamajig/Twiscord.git` in your parent directly to clone this repo into there. (**don't** create your own folder and cd into it, because clone makes the new folder either way)

4. Run this: `pipenv install` in this working directory, this will install all the necessary libraries through pipenv.

5. Create both Twitch bot and a Discord bot, and add them to your Discord Server and add as a Moderator on your Twitch Channel (guide for this WIP as of 2020/10/20) and follow the instructions in `example.env`. (make sure you rename that file to just `.env`)

6. Any time you want to run the bot, run this in the working directory: `pipenv run python .\main.py`

> How to install on Linux:

¯\\\_(ツ)\_/¯ WIP as of 2020/10/20

> How to install on MacOS:

¯\\\_(ツ)\_/¯ WIP as of 2020/10/20

## Is this open source / Can I contribute?
***Y E S***. If you have an idea that will improve this bot, make your changes and submit a pull request. Please keep the style consistant, other than that add whatever you want, as long as you think it will improve everyone's experience with this bot.

## What does this cost?
The cost of this app is entirely free, and all of its dependancies are free as well. The Twitch and Discord API's are free as long as you follow their rules (even then, you don't pay, you just get temp-banned or perma-banned). The only thing that could cost money is hosting. I recommend [Heroku](https://www.heroku.com) (not sponsored) as you get 550 free usage hours per month, but 1000 free usage hours per month if you validate your credit card. 550 hours would require you to manually turn on/off your bot through Heroku, but with the 1000 hours you could keep it on 100% for free (as long you don't have other scripts running)

## Licenses:
The license for Twiscord is an MIT License, except for code from the libraries, located [here](https://github.com/Samathingamajig/Twiscord/blob/master/LICENSE). The licenses for the libraries are downloaded through the `pipenv install`.

## Support:
If you need help, either create an Issue (for general problems), or join [this Discord Server](https://discord.gg/JH26PbJ) for your specific problems.

## Acknowledgements:
+ Samathingamajig: [Twitch](https://www.twitch.tv/samathingamajig) / Discord>Samathingamajig#5734 / [GitHub](https://github.com/Samathingamajig) » Creator
+ Rainbow_Helix: [Twitch](https://www.twitch.tv/rainbow_helix) » Requested this bot to exist, logo remixing 
+ 0vertime: [Twitch](https://www.twitch.tv/0vertimedev) / Discord>OverTime#7858 / [GitHub](https://github.com/0vertime-dev) » Bug testing
+ Discordpy, Twitchio, Asyncio devs » This bot would be much more complicated if these didn't exist.

## Legal stuff:
The Discord logo is copyright of Discord Inc. The Twitch logo is copyright of Twitch Interactive Inc. The Twiscord logo was a combined version of these two logos to show that this tool links Twitch and Discord together, remixing by Rainbow_Helix (see Acknowledgements)
