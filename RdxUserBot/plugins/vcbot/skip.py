from asyncio.queues import QueueEmpty
from pyrogram import filters
from pytgcalls.exceptions import GroupCallNotFound

from ... import app, eor, cdx, cdz
from ...modules.helpers.wrapper import *
from ...modules.mongo.streams import *
from ...modules.utilities import queues
from ...modules.utilities.streams import *


@app.on_message(cdx(["skp", "skip"]) & ~filters.private)
@sudo_users_only
async def skip_stream(client, message):
    chat_id = message.chat.id
    try:
        a = await call.get_call(chat_id)
        if (a.status == "playing"
            or a.status == "paused"
        ):
            queues.task_done(chat_id)
            if queues.is_empty(chat_id):
                await call.leave_group_call(chat_id)
                return await eor(message, "**£ɱקțÿ ǭɥ£ɥ£, So\nȽ£å√ȋñğ 𝓥𝓒!**")
            check = queues.get(chat_id)
            file = check["file"]
            type = check["type"]
            stream = await run_stream(file, type)
            await call.change_stream(chat_id, stream)
            return await eor(message, "**𝓢𝓽𝓻𝓮𝓪𝓶 𝓢𝓴𝓲𝓹𝓹𝓮𝓭!**")
        elif a.status == "not_playing":
            await eor(message, "**𝓝𝓸𝓽𝓱𝓲𝓷𝓰 𝓟𝓵𝓪𝔂𝓲𝓷𝓰!**")
    except GroupCallNotFound:
        await eor(message, "**𝓘 𝓪𝓶 𝓝𝓸𝓽 𝓲𝓷 𝓥𝓒!**")
    except Exception as e:
        print(f"Error: {e}")



@app.on_message(cdz(["cskp", "cskip"]) & ~filters.private)
@sudo_users_only
async def skip_stream_(client, message):
    user_id = message.from_user.id
    chat_id = await get_chat_id(user_id)
    if chat_id == 0:
        return await eor(message,
            "** 𝓝𝓸 𝓢𝓽𝓻𝓮𝓪𝓶 𝓒𝓱𝓪𝓽 𝓢𝓮 **"
    )
    try:
        a = await call.get_call(chat_id)
        if (a.status == "playing"
            or a.status == "paused"
        ):
            queues.task_done(chat_id)
            if queues.is_empty(chat_id):
                await call.leave_group_call(chat_id)
                return await eor(message, "**𝓔𝓶𝓹𝓽𝔂 𝓠𝓾𝓮𝓾𝓮, 𝓢𝓸\n𝓛𝓮𝓪𝓿𝓲𝓷𝓰 𝓥𝓒!**")
            check = queues.get(chat_id)
            file = check["file"]
            type = check["type"]
            stream = await run_stream(file, type)
            await call.change_stream(chat_id, stream)
            return await eor(message, "**ʂƚɾҽαɱ ʂƙιρρҽԃ!**")
        elif a.status == "not_playing":
            await eor(message, "**ɳσƚԋιɳɠ ρʅαყιɳɠ!**")
    except GroupCallNotFound:
        await eor(message, "**I am Not in VC!**")
    except Exception as e:
        print(f"Error: {e}")

