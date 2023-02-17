import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Kazu"])

async def join(client):
    try:
        await client.join_chat("DutabotSupport")
 	await client.join_chat("Arena4Me")
    except BaseException:
        pass
