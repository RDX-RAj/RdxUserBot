from ... import *
from ...modules.mongo.streams import *
from pyrogram import filters
from pytgcalls.exceptions import GroupCallNotFound


@app.on_message(cdx(["rsm", "resume"]) & ~filters.private)
@sudo_users_only
async def resume_stream(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if a.status == "paused":
            await call.resume_stream(chat_id)
            await eor(message, "**ˢᵗʳᵉᵃᵐ ʳᵉˢᵘᵐᵉᵈ!**")
        elif a.status == "playing":
            await eor(message, "**ᵃˡʳᵉᵃᵈʸ ᵖˡᵃʸⁱⁿᵍ!**")
        elif a.status == "not_playing":
            await eor(message, "**ⁿᵒᵗʰⁱⁿᵍ ˢᵗʳᵉᵃᵐⁱⁿᵍ!**")
    except GroupCallNotFound:
        await eor(message, "**ⁱ ᵃᵐ ⁿᵒᵗ ⁱⁿ ᵛᶜ!**")
    except Exception as e:
        print(f"Error: {e}")


@app.on_message(cdz(["crsm", "cresume"]))
@sudo_users_only
async def resume_stream_chat(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "**🥀 ⁿᵒ ˢᵗʳᵉᵃᵐ ᶜʰᵃᵗ ˢᵉᵗ❗**"
    )
    try:
        a = await call.get_call(chat_id)
        if a.status == "paused":
            await call.resume_stream(chat_id)
            await eor(message, "**ˢᵗʳᵉᵃᵐ ʳᵉˢᵘᵐᵉᵈ!**")
        elif a.status == "playing":
            await eor(message, "**𝘼𝙡𝙧𝙚𝙖𝙙𝙮 𝙋𝙡𝙖𝙮𝙞𝙣𝙜!**")
        elif a.status == "not_playing":
            await eor(message, "**𝙉𝙤𝙩𝙝𝙞𝙣𝙜 𝙎𝙩𝙧𝙚𝙖𝙢𝙞𝙣𝙜!**")
    except GroupCallNotFound:
        await eor(message, "**𝙄 𝙖𝙢 𝙉𝙤𝙩 𝙞𝙣 𝙑𝘾!**")
    except Exception as e:
        print(f"Error: {e}")

  
