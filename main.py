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


ERROR_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Report Bugs🤖", url="https://t.me/pikyus7"),
            InlineKeyboardButton("Learn Bot🙂", url="https://t.me/PTSMProject")
        ]
    ]
)

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
        await msg.edit_text(f"`{e}`", disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{link} `\n\n<a href=https://t.me/pikyus7>Feel free to leave a feedback</a>",
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
        await msg.edit_text(f"`{e}`", disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{link} `\n\n<a href=https://t.me/pikyus7>Feel free to leave a feedback</a>",
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
        await msg.edit_text(f"`{e}`", disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{link} `\n\n<a href=https://t.me/pikyus7>Feel free to leave a feedback</a>",
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
        await msg.edit_text(f"`{e}`", disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{link} `\n\n<a href=https://t.me/pikyus7>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)

print("🔥[BOT BERHASIL DIAKTIFKAN]🔥")

bot.run()
