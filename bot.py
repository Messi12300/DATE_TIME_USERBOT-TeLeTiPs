import asyncio
from os import environ
from pyrogram import Client, filters, idle

api_id = int(os.environ["API_ID"]),
api_hash = os.environ["API_HASH"],
session_name = os.environ["SESSION_NAME"]
BOT_TOKEN = environ.get("5039475558:AAGw4hIpCIfeoV3wyBerCwsdQNnenTAPd0o")
TIME = int(environ.get("1800"))
GROUPS = []
for grp in environ.get("-1001530674974").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("1154056577").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a simple bot to delete group messages after a specific time</b>"


User = Client(session_name=session_name,
              api_id=api_id,
              api_hash=api_hash,
              workers=300
              )


Bot = Client(session_name="auto-delete",
             api_id=api_id,
             api_hash=api_id,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.message_id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
