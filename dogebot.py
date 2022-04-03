import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")

LEBLANC = os.getenv("LEBLANC")
MORDEKAISER= os.getenv("MORDEKAISER")
KHAZIX = os.getenv("KHAZIX")
VAYNE = os.getenv("VAYNE")
KASSADIN = os.getenv("KASSADIN")
URGOT = os.getenv("URGOT")

LEBLANC_ID = int(os.getenv("LEBLANC_ID"))
MORDEKAISER_ID = int(os.getenv("MORDEKAISER_ID"))
KHAZIX_ID = int(os.getenv("KHAZIX_ID"))
VAYNE_ID = int(os.getenv("VAYNE_ID"))
KASSADIN_ID = int(os.getenv("KASSADIN_ID"))
URGOT_ID = int(os.getenv("URGOT_ID"))

help_message = """```
jungleduty
  - choose
        randomly pick a doge to carry out the jungle duty sentence
  - list
        display the official scroll of jungle duty sentences
  - assign [doge] [number]
        assign the chosen doge to [number] games of jungle duty
  - complete [doge] [number]
        complete [number] games from the official scroll for the chosen doge
```
"""

doge_ids = {
    LEBLANC: LEBLANC_ID,
    MORDEKAISER: MORDEKAISER_ID,
    KHAZIX: KHAZIX_ID,
    VAYNE: VAYNE_ID,
    KASSADIN: KASSADIN_ID,
    URGOT: URGOT_ID
}

responses = [
    "d0ge",
    "d0ge?",
    "d0ge!",
    "d0gon",
    "d0got",
    "d0gox",
    "d0gito",
    "d0gitar",
    "d0gothy",
    "d000ge!!",
    "d00000ge"
]

jungle_duty_dict = {
    LEBLANC: 0,
    URGOT: 0,
    MORDEKAISER: 0,
    VAYNE: 0,
    KHAZIX: 0,
    KASSADIN: 0
}

bot = commands.Bot(command_prefix="!", help_command=None)

@bot.event
async def on_message(message):
    if message.author != bot.user:
        if message.content.startswith("dog") or message.content.startswith("d0g"):
            response = "d00000000000000000000000000ge0ge!!!! 🐶🐶🐶" if message.author.id == URGOT_ID else random.choice(responses)
            await message.channel.send(response)
    await bot.process_commands(message)

@bot.command(name="jungleduty")
async def jungle_duty(ctx, *args):
    if len(args) == 0:
        await ctx.channel.send(help_message)
    elif len(args) == 1:
        if args[0] == "choose":
            chosen_jungler = random.choice(list(doge_ids.keys()))
            res = f"<@{doge_ids[chosen_jungler]}> is the new jungler! May summoner's rift tremble at {chosen_jungler}'s might."
            await ctx.channel.send(res)
        elif args[0] == "list":
            s = '\n'.join(f" - {k}: {v}" for k, v in jungle_duty_dict.items())
            res = f"```SCROLL OF JUNGLE DUTIES\n{s}```"
            await ctx.channel.send(res)
        else:
            await ctx.channel.send(f"\"{args[0]}\" is an invalid argument, retoge.")
    elif len(args) == 2:
        if args[0] in ["choose", "list", "assign", "complete"]:
            if args[1] in jungle_duty_dict:
                if args[0] == "choose":
                    res = f"<@{doge_ids[args[1]]}> is the new jungler! May summoner's rift tremble at {args[1]}'s might."
                    await ctx.channel.send(res)
                elif args[0] == "list":
                    res = f"<@{doge_ids[args[1]]}> has {jungle_duty_dict[args[1]]} sentences remaining."
                    await ctx.channel.send(res)
                elif args[0] == "assign":
                    await ctx.channel.send(f"You must provide a number to assign to {args[1]}, retoge.")
                else:
                    await ctx.channel.send(f"You must provide a number to complete for {args[1]}, retoge.")
            else:
                await ctx.channel.send(f"Wait wot? who is {args[1]}?")
        else:
            await ctx.channel.send(f"\"{args[0]}\" is an invalid argument, retoge.")
    elif len(args) == 3:
        if args[0] == "assign" or args[0] == "complete":
            if args[1] in jungle_duty_dict:
                if args[2].isdigit():
                    if int(args[2]) > 0:
                        if args[0] == "assign":
                            jungle_duty_dict[args[1]] += int(args[2])
                            jd = f"<@{doge_ids[args[1]]}> is hereby sentenced to {args[2]} game{'s' if args[2] != 1 else None} of jungle duty!"
                            res = f"{jd}\n<@{doge_ids[args[1]]}> has {jungle_duty_dict[args[1]]} sentences remaining."
                            await ctx.channel.send(res)
                        else:
                            if int(args[2]) <= jungle_duty_dict[args[1]]:
                                jungle_duty_dict[args[1]] -= int(args[2])
                                jd = f"Let the almighty d0ge bear witness that <@{doge_ids[args[1]]}> has completed {args[2]} game{'s' if args[2] != 1 else None} of jungle duty!"
                                res = f"{jd}\n<@{doge_ids[args[1]]}> has {jungle_duty_dict[args[1]]} sentences remaining."
                                await ctx.channel.send(res)
                            else:
                                await ctx.channel.send(f"{args[1]} cannot complete more games than he is assigned, retoge.")
                    else:
                        await ctx.channel.send(f"The number of has to be greater than 0, retoge.")
                else:
                    await ctx.channel.send(f"{args[2]} isn't a number, retoge.")
            else:
                await ctx.channel.send(f"Wait wot? who is {args[1]}?")
        else:
            await ctx.channel.send(f"\"{args[0]}\" is an invalid argument, retoge.")
    else:
        await ctx.channel.send(f"wot\n(invalid number of arguments)")
    
bot.run(TOKEN)
