# Copyright (C) 2022 szsupunma
# Copyright (C) 2021 @szrosebot

# This file is part of @szrosebot (Telegram Bot)

from Rose import bot as app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton,InlineKeyboardMarkup

text = """
Rose was created on **August 10, 2021**. We are currently developing and maintaining the **WilliamButcherBot**  and **Alita_Robot** plugin, using only the Pyrogram libarry.

• [support group](https://t.me/TamilSupport) 
• [News Channel](https://t.me/TamilBots) 
• [Documentation](https://imsaravanakrish.gitbook.io/imsaravanakrish/)
• [Logs Channel](https://t.me/TamilBots)
• [Network](https://t.me/TamilBotZ)
• [Source Code](https://github.com/ImSaravanakrish)

**Current Version:** `1.0.8` | [Changelogs](https://imsaravanakrish.gitbook.io/imsaravanakrish/changelogs)
"""

fbuttons = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('« Back', callback_data='startcq')
        ]]
)

@app.on_callback_query(filters.regex("_about"))
async def commands_callbacc(_, CallbackQuery):
    await app.send_message(
        CallbackQuery.message.chat.id,
        text=text,
        reply_markup=fbuttons,
        disable_web_page_preview=True,
    )
    await CallbackQuery.message.delete()
