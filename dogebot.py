import os
import random

import boto3
import discord
from discord.ext import commands
from dotenv import load_dotenv


# Load all environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")
CHANNEL = int(os.getenv("DISCORD_CHANNEL"))

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION")

LEBLANC = os.getenv("LEBLANC")
MORDEKAISER = os.getenv("MORDEKAISER")
KHAZIX = os.getenv("KHAZIX")
VAYNE = os.getenv("VAYNE")
KASSADIN = os.getenv("KASSADIN")
URGOT = os.getenv("URGOT")
EZREAL = os.getenv("EZREAL")

LEBLANC_ID = int(os.getenv("LEBLANC_ID"))
MORDEKAISER_ID = int(os.getenv("MORDEKAISER_ID"))
KHAZIX_ID = int(os.getenv("KHAZIX_ID"))
VAYNE_ID = int(os.getenv("VAYNE_ID"))
KASSADIN_ID = int(os.getenv("KASSADIN_ID"))
URGOT_ID = int(os.getenv("URGOT_ID"))
EZREAL_ID = int(os.getenv("EZREAL_ID"))

# Map username to ID
doge_ids = {
    LEBLANC: LEBLANC_ID,
    MORDEKAISER: MORDEKAISER_ID,
    KHAZIX: KHAZIX_ID,
    VAYNE: VAYNE_ID,
    KASSADIN: KASSADIN_ID,
    URGOT: URGOT_ID,
    EZREAL: EZREAL_ID
}


# Connect to AWS DynamoDB
client = boto3.client(
    "dynamodb",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)

dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)

table = dynamodb.Table("jungleduty")


# Initialize bot
intents = discord.Intents.default()
intents.members = True

help_command = commands.DefaultHelpCommand(no_category="dogeb0t commands")

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or('!'),
    help_command=help_command,
    intents=intents
)


# ------------------
#      COMMANDS
# ------------------

responses = ["d0ge", "d0ge?", "d0ge!", "d0gon", "d0got", "d0gox", "d0gito", "d0gitar", "d0gothy", "d000ge!!", "d00000ge"]

dogical_responses = [
    ("Long time no see, ", " ", "🥺"),
    ("I've missed you, ", " ", "😉😘"),
    ("Hey ", ", you're looking quite dogical tonight ", "😜💦"),
    ("Oh my d0ge, it's ", " ", "❗️"),
    ("Scooby dooby ", ", where are th0ge ", "🐶")
]

@bot.event
async def on_message(message):
    if message.author != bot.user:
        if message.content.startswith("dog") or message.content.startswith("d0g"):
            response = random.choice(responses)
            if message.author.id == URGOT_ID:
                doge_str = f"d{'0' * random.randint(2,5)}ge"
                temp = random.choice(dogical_responses)
                response = f"{temp[0]}{doge_str}{temp[1]}{temp[2] * random.randint(1,5)}"
            await message.channel.send(response)
    await bot.process_commands(message)


@bot.command(
    help="Lists members of the channel",
    brief="Lists members of the channel"
)
async def members(ctx):
    for member in ctx.channel.members:
        await ctx.channel.send(f"{member} - id={member.id}")


@bot.command(
	help="Repeats the message you sent back to you",
	brief="Repeats the message you sent back to you"
)
async def say(ctx, *args):
	await ctx.channel.send(f"{' '.join(args)}")


@bot.command(
    help="Whispers the message you sent in the main channel",
    brief="Whispers the message in the main channel"
)
async def whisper(ctx, *args):
    channel = bot.get_channel(CHANNEL)
    await channel.send(f"{' '.join(args)}")


@bot.command(
    help="Speaks the message you sent in the main channel using /tts",
    brief="Speaks the message in the main channel"
)
async def speak(ctx, *args):
    channel = bot.get_channel(CHANNEL)
    await channel.send(f"{' '.join(args)}", tts=True)


@bot.command(
    help="Fuk [insert doge]",
    brief="Fuk [insert doge]"
)
async def fuk(ctx, *args):
    if args[0] in doge_ids:
        summoner_id = doge_ids[args[0]]
        res = f"fuck you <@{summoner_id}>"
        if len(args) >= 2 and args[1] == "*":
            res = f"FUCK YOU <@{summoner_id}>"
        for _ in range(random.randint(5, 10)):
            await ctx.channel.send(res)


jungle_help = """
  - choose
        randomly pick a doge to carry out the jungle duty sentence
  - list
        display the official scroll of jungle duty sentences
  - assign [doge] [number]
        assign the chosen doge to [number] games of jungle duty
  - complete [doge] [number]
        complete [number] games from the official scroll for the chosen doge
"""
@bot.command(
    name="jungleduty",
    help=jungle_help,
    brief="Keeps track of jungle duties"
)
async def jungle_duty(ctx, *args):
    if len(args) == 0:
        await ctx.channel.send(f"```jungleduty {jungle_help}```")
    elif len(args) == 1:
        if args[0] == "choose":
            chosen_jungler = random.choice(list(doge_ids.keys()))
            res = f"<@{doge_ids[chosen_jungler]}> is the new jungler! May summoner's rift tremble at {chosen_jungler}'s might."
            await ctx.channel.send(res)
        elif args[0] == "list":
            request = table.scan()
            s = '\n'.join(f" - {d['name']}: {d['games']}" for d in request["Items"])
            res = f"```SCROLL OF JUNGLE DUTIES\n{s}```"
            await ctx.channel.send(res)
        else:
            await ctx.channel.send(f"\"{args[0]}\" is an invalid argument, retoge.")
    elif len(args) == 2:
        if args[0] in ["choose", "list", "assign", "complete"]:
            if args[1] in doge_ids:
                if args[0] == "choose":
                    res = f"<@{doge_ids[args[1]]}> is the new jungler! May summoner's rift tremble at {args[1]}'s might."
                    await ctx.channel.send(res)
                elif args[0] == "list":
                    request = table.get_item(Key={"name": args[1]})
                    await ctx.channel.send(f"<@{doge_ids[args[1]]}> has {request['Item']['games']} sentences remaining.")
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
            if args[1] in doge_ids:
                if args[2].isdigit():
                    if int(args[2]) > 0:
                        request = table.get_item(Key={"name": args[1]})
                        games = request["Item"]["games"]
                        if args[0] == "assign":
                            games += int(args[2])
                            table.update_item(
                                Key={"name": args[1]},
                                UpdateExpression="set games = :g",
                                ExpressionAttributeValues={":g": games},
                                ReturnValues="UPDATED_NEW"
                            )
                            sentence = f"<@{doge_ids[args[1]]}> is hereby sentenced to {args[2]} game{'s' if args[2] != '1' else ''} of jungle duty!"
                            res = f"{sentence}\n<@{doge_ids[args[1]]}> has {games} sentences remaining."
                            await ctx.channel.send(res)
                        else:
                            if int(args[2]) <= games:
                                games -= int(args[2])
                                table.update_item(
                                    Key={"name": args[1]},
                                    UpdateExpression="set games = :g",
                                    ExpressionAttributeValues={":g": games},
                                    ReturnValues="UPDATED_NEW"
                                )
                                sentence = f"Let the almighty d0ge bear witness that <@{doge_ids[args[1]]}> has completed {args[2]} game{'s' if args[2] != '1' else ''} of jungle duty!"
                                res = f"{sentence}\n<@{doge_ids[args[1]]}> has {games} sentences remaining."
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

 
# Run bot
bot.run(TOKEN)