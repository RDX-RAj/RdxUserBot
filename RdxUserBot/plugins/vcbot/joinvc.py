from ... import *
from ...modules.mongo.streams import *
from pyrogram import filters
from pytgcalls.exceptions import GroupCallNotFound


@app.on_message(cdx(["join", "joinvc"]) & ~filters.private)
@sudo_users_only
async def join_vc(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if (a.status == "not_playing"
            or a.status == "playing"
            or a.status == "paused"
        ):
            await eor(message, "**αℓяєα∂у נσιηє∂!**")
    except GroupCallNotFound:
        await call.join_group_call(chat_id)
        await eor(message, "**נσιηє∂ ν¢!**")
    except Exception as e:
        print(f"Error: {e}")


@app.on_message(cdz(["cjoin", "cjoinvc"]))
@sudo_users_only
async def join_vc_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "**» ησ ѕтяєαм ¢нαт ѕєт❗**"
    )
    try:
        a = await call.get_call(chat_id)
        if (a.status == "not_playing"
            or a.status == "playing"
            or a.status == "paused"
        ):
            await eor(message, "**𝙰𝚕𝚛𝚎𝚊𝚍𝚢 𝙹𝚘𝚒𝚗𝚎𝚍!**")
    except GroupCallNotFound:
        await call.join_group_call(chat_id)
        await eor(message, "**𝙹𝚘𝚒𝚗𝚎𝚍 𝚅𝙲!**")
    except Exception as e:
        print(f"Error: {e}")
