import asyncio
from time import time
from datetime import datetime
from config import BOT_USERNAME
from config import GROUP_SUPPORT, UPDATES_CHANNEL, START_PIC
from Zaid.filters import command
from Zaid.command import commandpro
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Zaid.main import bot as Client

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""A Telegram Music Bot('JBL VC BOT') Based PyroGram.

💞 **Main Features**
~ Support Audio + Video Stream
~ YouTube/Local/Live/m3u8 stream support
~ Voice Raid / Video Raid
~ Spam, Bigspam, Raid and LoveRaid
~ Audio And Video Download from YouTube

Powered By [SUMIT ʙᴏᴛꜱ](t.me/iMi_SuMiT_Op) ...
""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "°OWNER°", url=f"https://t.me/iMi_SuMiT_Op"
                    ),
                    InlineKeyboardButton(
                        "ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/opsumitop/Zaid-Vc-Player"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📢 ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/Unknown_tg_world"
                    ),
                    InlineKeyboardButton(
                        "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 🇮🇳", url=f"https://t.me/Unknown_tg_world"
                    )
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/stats"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/876afe3b91296bf8ed00c.jpg",
        caption=f"""Thanks For Adding Me To Ur Chat, For Any Query U Can Join Our Support Groups 🔥♥️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ 💞", url=f"https://t.me/Unknown_tg_world")
                ]
            ]
        ),
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/876afe3b91296bf8ed00c.jpg",
        caption=f"""Here Is The Source Code Fork And Give Stars ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ⚒️", url=f"https://github.com/opsumitop/Zaid-Vc-Player")
                ]
            ]
        ),
    )
