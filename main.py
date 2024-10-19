import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from catbox import CatboxUploader, CatboxError
from config import Config

bot = Client(
    "bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

INLINE_SELECT = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Github🤩", url="https://github.com/SendiAp/catbox-uploader-bot"),
            InlineKeyboardButton("Report Bugs🤖", url="https://t.me/pikyus7")
        ],
        [
            InlineKeyboardButton("Join Channel🌐", url="https://t.me/PTSMProject")
        ]
    ]
)

ERROR_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Report Bugs🤖", url="https://t.me/pikyus7"),
            InlineKeyboardButton("Learn Bot🙂", url="https://t.me/PTSMProject")
        ]
    ]
)

@bot.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    text = f"Hello {message.from_user.first_name}!\n\nSelamat datang di bot pengunggah catbox.\nAnda dapat mengirimi saya apa pun " \
           f"image, video, animation dan saya akan mengunggahnya ke catbox dan mengirimkan tautan yang dibuat. Namun, file tersebut harus berukuran KURANG DARI 5MB!!\n\n" \
           f"<a href=https://t.me/PTSNProject>Bebas meninggalkan umpan balik</a>"
    reply_markup = INLINE_SELECT
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True)

## UPLOAD PHOTOS
uploader = CatboxUploader()

@bot.on_message(filters.photo & filters.private)
async def photo_upload(bot, message):
    msg = await message.reply("Uploading", quote=True)
    download_path = await bot.download_media(message)
    try:
        link = uploader.upload_file(download_path)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Link Preview", url=f"{link}")
                ]
            ]

        )
    except CatboxError as e:
        return await msg.edit_text(f"`{e}`", disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(link, disable_web_page_preview=True)
        return await t.edit_text(
            f"Link - `{link} `\n\n© Catbox Uploader",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)
        
## UPLOAD VIDEOS
@bot.on_message(filters.video & filters.private)
async def video_upload(bot, message):
    msg = await message.reply("Uploading", quote=True)
    download_path = await bot.download_media(message)
    try:
        link = uploader.upload_file(download_path)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Link Preview", url=f"{link}")
                ]
            ]

        )
    except CatboxError as e:
        return await msg.edit_text(f"`{e}`", disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(link, disable_web_page_preview=True)
        return await t.edit_text(
            f"Link - `{link} `\n\n© Catbox Uploader",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)

## UPLOAD GIF
@bot.on_message(filters.animation & filters.private)
async def animation_upload(bot, message):
    msg = await message.reply("Uploading", quote=True)
    download_path = await bot.download_media(message)
    try:
        link = uploader.upload_file(download_path)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Link Preview", url=f"{link}")
                ]
            ]

        )
    except CatboxError as e:
        return await msg.edit_text(f"`{e}`", disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(link, disable_web_page_preview=True)
        return await t.edit_text(
            f"Link - `{link} `\n\n© Catbox Uploader",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)

## STICKER UPLOAD
@bot.on_message(filters.sticker)
async def sticker_upload(bot, message):
    msg = await message.reply("Uploading", quote=True)
    download_path = await bot.download_media(message)
    try:
        link = uploader.upload_file(download_path)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Link Preview", url=f"{link}")
                ]
            ]

        )
    except CatboxError as e:
        return await msg.edit_text(f"`{e}`", disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(link, disable_web_page_preview=True)
        return await t.edit_text(
            f"Link - `{link} `\n\n© Catbox Uploader",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)

print("🔥[BOT BERHASIL DIAKTIFKAN]🔥")

bot.run()
