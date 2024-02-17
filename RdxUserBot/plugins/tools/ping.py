from ... import *
from datetime import datetime

@app.on_message(cdx("ping"))
@sudo_users_only
async def ping(client, message):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    m = await eor(message, "**🤖 Ping !**")
    await m.edit(f"**» ᴘɪɴɢᴇᴅ !\nʟᴀᴛᴇɴᴄʏ:** `{ms}` ms")



__NAME__ = "Ping"
__MENU__ = """
`.ping` - **ᴄʜᴇᴄᴋ ᴘɪɴɢ ʟᴀᴛᴇɴᴄʏ
ᴏғ ʏᴏᴜʀ ᴜsᴇʀʙᴏᴛ sᴇʀᴠᴇʀ.**
"""
