from ... import *
from ...modules.mongo.streams import *
from pyrogram import filters
from pytgcalls.exceptions import GroupCallNotFound


@app.on_message(cdx(["pse", "pause"]) & ~filters.private)
@sudo_users_only
async def pause_stream(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if a.status == "playing":
            await call.pause_stream(chat_id)
            await eor(message, "**ṡṭяєѧṃ ƿѧȗṡєԀ!**")
        elif a.status == "paused":
            await eor(message, "**ѧʟяєѧԀʏ ƿѧȗṡєԀ!**")
        elif a.status == "not_playing":
            await eor(message, "**ṅȏṭһıṅɢ ṡṭяєѧṃıṅɢ!**")
    except GroupCallNotFound:
        await eor(message, "**ı ѧṃ ṅȏṭ ıṅ ṿċ!**")
    except Exception as e:
        print(f"Error: {e}")


@app.on_message(cdz(["cpse", "cpause"]))
@sudo_users_only
async def pause_stream_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "** ℕ𝕠 𝕊𝕥𝕣𝕖𝕒𝕞 ℂ𝕙𝕒𝕥 𝕊𝕖𝕥❗**"
    )
    try:
        a = await call.get_call(chat_id)
        if a.status == "playing":
            await call.pause_stream(chat_id)
            await eor(message, "**𝕊𝕥𝕣𝕖𝕒𝕞 ℙ𝕒𝕦𝕤𝕖𝕕!**")
        elif a.status == "paused":
            await eor(message, "**𝔸𝕝𝕣𝕖𝕒𝕕𝕪 ℙ𝕒𝕦𝕤𝕖𝕕!**")
        elif a.status == "not_playing":
            await eor(message, "**ℕ𝕠𝕥𝕙𝕚𝕟𝕘 𝕊𝕥𝕣𝕖𝕒𝕞𝕚𝕟𝕘!**")
    except GroupCallNotFound:
        await eor(message, "**I̶̶ a̶̶m̶̶ N̶̶o̶̶t̶̶ i̶̶n̶̶ V̶̶C̶̶!**")
    except Exception as e:
        print(f"Error: {e}")

  
