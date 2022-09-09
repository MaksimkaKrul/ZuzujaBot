# Бот Discord
import discord
import emoji
from discord.ext import commands
from setings import discord_t


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='$', intents=intents)
last_news = ['1', '2', '3']
announcements = ['a', 'b', 'c']



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    channel_announcement = client.get_channel(1014176783173681174)
    channel_news = client.get_channel(1017486748021960704)
    #For announcements
    announcement_messages = [message async for message in channel_announcement.history(limit=3)]
    for message in announcement_messages:
        announcements.append(message.content)
        announcements.pop(0)
    # contest[2] = discordemoji.replace(contest[2], rep="")
    # contest[1] = discordemoji.replace(contest[1], rep="")
    # contest[0] = discordemoji.replace(contest[0], rep="")
    announcements[2] = emoji.demojize(announcements[2])
    announcements[1] = emoji.demojize(announcements[1])
    announcements[0] = emoji.demojize(announcements[0])
    for i in range(len(announcements)):
        with open('lastmessage1.txt', 'w') as f:
            f.write('\n\n-----------------------------------\n\n'.join([str(i) for i in announcements]) + '\n')

    #For news
    news_messages = [message async for message in channel_news.history(limit=3)]
    for message in news_messages:
        last_news.append(message.content)
        last_news.pop(0)
    # contest[2] = discordemoji.replace(contest[2], rep="")
    # contest[1] = discordemoji.replace(contest[1], rep="")
    # contest[0] = discordemoji.replace(contest[0], rep="")
    last_news[2] = emoji.demojize(last_news[2])
    last_news[1] = emoji.demojize(last_news[1])
    last_news[0] = emoji.demojize(last_news[0])
    for i in range(len(last_news)):
        with open('lastmessage2.txt', 'w') as f:
            f.write('\n\n-----------------------------------\n\n'.join([str(i) for i in last_news]) + '\n')


@client.event
async def on_message(message):
    channel_announcement = client.get_channel(1014176783173681174)
    channel_news = client.get_channel(1017486748021960704)

    #For announcements
    if message.channel == channel_announcement:
        new_announcement = [message async for message in channel_announcement.history(limit=3)]
        for message in new_announcement:
            message_strip = message.content.strip()
            announcements.append(message_strip)
            announcements.pop(0)
        announcements.reverse()
        announcements[2] = emoji.demojize(announcements[2])
        announcements[1] = emoji.demojize(announcements[1])
        last_message_announcements = emoji.demojize(message.content)
        if message.channel == channel_announcement:
            if message.attachments:
                announcements[2], announcements[1], announcements[0] = last_message_announcements + " " + message.attachments[0].url, \
                                                                    announcements[1], announcements[2]
            else:
                announcements[2], announcements[1], announcements[0] = last_message_announcements, announcements[1], announcements[2]
        for i in range(len(announcements)):
            with open('lastmessage1.txt', 'w') as f:
                f.write('\n\n-----------------------------------\n\n'.join([str(i) for i in announcements]) + '\n')


    # For news
    if message.channel == channel_news:
        new_news = [message async for message in channel_news.history(limit=3)]
        for message in new_news:
            message_strip = message.content.strip()
            last_news.append(message_strip)
            last_news.pop(0)
        last_news.reverse()
        last_news[2] = emoji.demojize(last_news[2])
        last_news[1] = emoji.demojize(last_news[1])
        last_message_news = emoji.demojize(message.content)
        if message.channel == channel_news:
            if message.attachments:
                last_news[2], last_news[1], last_news[0] = last_message_news + " " + message.attachments[0].url, \
                                                                    last_news[1], last_news[2]
            else:
                last_news[2], last_news[1], last_news[0] = last_message_news, last_news[1], last_news[2]
        for i in range(len(last_news)):
            with open('lastmessage2.txt', 'w') as f:
                f.write('\n\n-----------------------------------\n\n'.join([str(i) for i in last_news]) + '\n')



client.run(discord_t)
