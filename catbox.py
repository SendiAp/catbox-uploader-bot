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
            InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot"),
            InlineKeyboardButton("Learn Bot🙂", url="https://t.me/sanilaassistant_bot")
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
                    InlineKeyboardButton("Github🤩", url="https://github.com/catbox-uploader-bot"),
                    InlineKeyboardButton("Report Bugs🤖", url="https://t.me/pikyus7")
                ],
                [
                    InlineKeyboardButton("Web Preview🌐", urlf"{link}")
                ]
            ]

        )
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{link} `\n\n<a href=https://t.me/pikyus7>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)
        
## UPLOAD VIDEOS

@bot.on_message(filters.video & filters.private)
async def video_upload(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="image/jetg")
    try:
        link = upload_file(download_path)
        generated_Link = "https://telegra.ph" + "".join(link)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Github🤩", url="https://github.com/sanila2007"),
                    InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot")
                ],
                [
                    InlineKeyboardButton("Web Preview🌐", url=generated_Link)
                ]
            ]
        )
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            disable_web_page_preview=True, reply_markup=ERROR_BUTTON)
    else:
        t = await msg.edit_text(generated_Link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_Link} `\n\n<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)

## UPLOAD GIF
@bot.on_message(filters.animation & filters.private)
async def animation_upload(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Github🤩", url="https://github.com/sanila2007"),
                    InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot")
                ],
                [
                    InlineKeyboardButton("Web Preview🌐", url=generated_link)
                ]
            ]
        )
    except:
        await msg.edit_text(
            "File must be less than 5mb, please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)

## STICKER UPLOAD
@bot.on_message(filters.sticker)
async def sticker_upload(bot, message):
    msg = await message.reply("Your file is been uploading...", quote=True)
    download_path = await bot.download_media(message=message, file_name="gif/jetg")
    try:
        link = upload_file(download_path)
        generated_link = "https://telegra.ph" + "".join(link)
        IN_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Github🤩", url="https://github.com/sanila2007"),
                    InlineKeyboardButton("Report Bugs🤖", url="https://t.me/sanilaassistant_bot")
                ],
                [
                    InlineKeyboardButton("Web Preview🌐", url=generated_link)
                ]
            ]
        )
    except Exception as a:
        await msg.edit_text(
            f"❌ This sticker was unable to upload. Please try another file or <a href=https://t.me/sanilaassistant_bot>LEARN THIS BOT FIRST!</a>\n\n<i>Caused error - {a}</i>",
            reply_markup=INLINE_SELECT,
            disable_web_page_preview=True)
    else:
        t = await msg.edit_text(generated_link, disable_web_page_preview=True)
        await t.edit_text(
            f"Link - `{generated_link} `\n\n<a href=https://t.me/sanilaassistant_bot>Feel free to leave a feedback</a>",
            reply_markup=IN_BUTTON,
            disable_web_page_preview=True)
    finally:
        os.remove(download_path)

print("🔥[BOT BERHASIL DIAKTIFKAN]🔥")

bot.run()
