from asyncio.queues import QueueEmpty
from pyrogram import filters
from pytgcalls.exceptions import GroupCallNotFound

from ... import *
from ...modules.mongo.streams import *
from ...modules.utilities import queues


@app.on_message(cdx(["lve", "rdxlve", "leave", "leavevc"]) & ~filters.private)
@sudo_users_only
async def leave_vc(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if (a.status == "not_playing"
            or a.status == "playing"
            or a.status == "paused"
        ):  
            try:
                queues.clear(chat_id)
            except QueueEmpty:
                pass
            await call.leave_group_call(chat_id)
            await eor(message, "**ʟᴇғᴛ ᴠᴄ**")
    except GroupCallNotFound:
        await eor(message, "**ɪ ᴀᴍ ɴᴏᴛ ɪɴ ᴠᴄ**")
    except Exception as e:
        print(f"Error: {e}")


@app.on_message(cdz(["clve", " rdxclve", "cleave", "cleavevc"]))
@sudo_users_only
async def leave_vc_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "** ɴᴏ sᴛʀᴇᴀᴍ ɴᴏᴛ sᴇᴛ**"
    )
    try:
        a = await call.get_call(chat_id)
        if (a.status == "not_playing"
            or a.status == "playing"
            or a.status == "paused"
        ):  
            try:
                queues.clear(chat_id)
            except QueueEmpty:
                pass
            await call.leave_group_call(chat_id)
            await eor(message, "**ʟᴇғᴛ ᴠᴄ**")
    except GroupCallNotFound:
        await eor(message, "**ı ᴀᴍ ɴᴏᴛ ɪɴ ᴠᴄ!**")
    except Exception as e:
        print(f"Error: {e}")
