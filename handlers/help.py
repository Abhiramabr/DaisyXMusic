from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

PM_HELP_TEXT = """Commands 🛠
For all in group

    /play - reply to youtube url or song file to play song
    /play <song name> - play song you requested
    /song <song name> - download songs you want quickly
    /search <query> - search videos on youtube with details

Admins only

    /pause - pause song play
    /resume - resume song play
    /skip - play next song
    /end - stop music play
""" 

@Client.on_message(filters.command(["help"]))
async def help(client, message):
    await message.reply_text(
     PM_HELP_TEXT, 
     reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🛸 Support', url='https://t.me/Wandabetaxbot')
                ]
            ]
        )
    ) 
