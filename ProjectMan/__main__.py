# Credits: @mrismanaziz & @excute7
# Copyright (C) 2022 Hyper-Userbot
#
# This file is a part of < https://github.com/Ling-ex/Hyper/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/Ling-ex/Hyper/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de
# t.me/HyperSupportQ & t.me/storyQi

import importlib

from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from ProjectMan import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots
from ProjectMan.helpers.misc import create_botlog, heroku
from ProjectMan.modules import ALL_MODULES

MSG_ON = """
🔥 **Hyper-Userbot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
━━
"""


async def main():
    for all_module in ALL_MODULES:
        importlib.import_module(f"ProjectMan.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            await bot.join_chat("storyQi")
            await bot.join_chat("HyperSupportQ")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("ProjectMan").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("ProjectMan").info(f"Hyper-UserBot v{BOT_VER} [🔥 BERHASIL DIAKTIFKAN! 🔥]")
    if bot1 and not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("ProjectMan").info("Starting Hyper-UserBot")
    install()
    heroku()
    LOOP.run_until_complete(main())
