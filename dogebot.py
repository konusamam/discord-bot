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
VC1 = int(os.getenv("DISCORD_VOICE_CHANNEL_1"))
VC2 = int(os.getenv("DISCORD_VOICE_CHANNEL_2"))
VC3 = int(os.getenv("DISCORD_VOICE_CHANNEL_3"))

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

str1 = os.getenv("STR1")
str2 = os.getenv("STR2")

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


# Lowercase dicts for case-insensitive lookup
doge_ids_lower = {k.lower(): v for k, v in doge_ids.items()}
doge_names_lower = {k.lower(): k for k in doge_ids.keys()}


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
activity = discord.Activity(type=discord.ActivityType.listening, name="the d0ges")

bot = commands.Bot(
    command_prefix=commands.when_mentioned_or("!"),
    help_command=help_command,
    activity=activity,
    intents=intents
)


# Helper method for looking up doge names
def lookup_doge(name):
    if name.lower() not in doge_ids_lower:
        return None
    
    doge = {
        "name": doge_names_lower[name.lower()],
        "id": doge_ids_lower[name.lower()]
    }
    return doge


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
                doge_str = f"d{'0' * random.randint(3,10)}ge"
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


@bot.command()
async def join_voice_channel(ctx, *args):
    channel_id = 0

    if len(args) != 1:
        return
    elif args[0] == "a":
        channel_id = VC1
    elif args[0] == "p":
        channel_id = VC2
    elif args[0] == "t":
        channel_id = VC3

    if not channel_id:
        return
    
    vc = bot.get_channel(channel_id)
    await vc.connect()


@bot.command()
async def leave_voice_channel(ctx, *args):
    channel_id = 0

    if len(args) != 1:
        return
    elif args[0] == "a":
        channel_id = VC1
    elif args[0] == "p":
        channel_id = VC2
    elif args[0] == "t":
        channel_id = VC3

    if not channel_id:
        return
    
    vc = bot.get_channel(channel_id)
    await vc.disconnect()


@bot.command(
    help="f [insert doge]",
    brief="f [insert doge]"
)
async def f(ctx, *args):
    doge = lookup_doge(args[0])
    if doge:
        res = f"{str1} <@{doge['id']}>"
        if len(args) >= 2 and args[1] == "*":
            res = f"{str1.upper()} <@{doge['id']}>"
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
            await ctx.channel.send(f"\"{args[0]}\" is an invalid argument, {str2}.")

    elif len(args) == 2:
        doge = lookup_doge(args[1])

        # Invalid username
        if not doge:
            await ctx.channel.send(f"Wait wot? who is {args[1]}?")
            return

        if args[0] == "choose":
            res = f"<@{doge['id']}> is the new jungler! May summoner's rift tremble at {doge['name']}'s might."
            await ctx.channel.send(res)
        elif args[0] == "list":
            request = table.get_item(Key={"name": doge["name"]})
            await ctx.channel.send(f"<@{doge['id']}> has {request['Item']['games']} sentences remaining.")
        elif args[0] == "assign":
            await ctx.channel.send(f"You must provide a number to assign to {doge['name']}, {str2}.")
        elif args[0] == "complete":
            await ctx.channel.send(f"You must provide a number to complete for {doge['name']}, {str2}.")
        else:
            await ctx.channel.send(f"\"{args[0]}\" is an invalid argument, {str2}.")


    elif len(args) == 3:
        doge = lookup_doge(args[1])

        # Invalid username
        if not doge:
            await ctx.channel.send(f"Wait wot? who is {args[1]}?")
            return

        # Invalid argument
        if args[0] != "assign" and args[0] != "complete":
            await ctx.channel.send(f"\"{args[0]}\" is an invalid argument, {str2}.")
            return

        # Invalid number of games
        if int(args[2]) <= 0:
            await ctx.channel.send(f"The number of games has to be greater than 0, {str2}.")
            return
        elif not args[2].isdigit():
            await ctx.channel.send(f"{args[2]} isn't a number, {str2}.")
            return

        # Perform update
        request = table.get_item(Key={"name": doge["name"]})
        games = request["Item"]["games"]

        if args[0] == "assign":
            games += int(args[2])
            table.update_item(
                Key={"name": doge["name"]},
                UpdateExpression="set games = :g",
                ExpressionAttributeValues={":g": games},
                ReturnValues="UPDATED_NEW"
            )
            sentence = f"<@{doge['id']}> is hereby sentenced to {args[2]} game{'s' if args[2] != '1' else ''} of jungle duty!"
            res = f"{sentence}\n<@{doge['id']}> has {games} sentence{'s' if games != 1 else ''} remaining."
            await ctx.channel.send(res)
        else:
            if int(args[2]) > games:
                await ctx.channel.send(f"{doge['name']} cannot complete more games than he is assigned, {str2}.")
                return

            games -= int(args[2])
            table.update_item(
                Key={"name": doge['name']},
                UpdateExpression="set games = :g",
                ExpressionAttributeValues={":g": games},
                ReturnValues="UPDATED_NEW"
            )
            sentence = f"Let the almighty d0ge bear witness that <@{doge['id']}> has completed {args[2]} game{'s' if args[2] != '1' else ''} of jungle duty!"
            res = f"{sentence}\n<@{doge['id']}> has {games} sentence{'s' if games != 1 else ''} remaining."
            await ctx.channel.send(res)


# Run bot
bot.run(TOKEN)