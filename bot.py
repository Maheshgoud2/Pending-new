import logging
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, PeerIdInvalid, RPCError

logging.basicConfig(level=logging.ERROR)

API_ID = "20959976"
API_HASH = "4f648d2c4c0fd1b89a995bb85b2dba67"

app = Client("1AZWarzIAUKGaqbfsjfFYWPkC7VBzgTvSMW3QAN1SdqFURXbB5pP01nk86nSDON3v_uLsFTByt7BPRdEX9NPnbm3-LSmWZ__EsCa6yjUwN2UQMXniTX2MMawsM01HkT_syiMoTzlaGz1cMIE1niDJs62L4Vo-DFMgNK_CiJzsUkzpEQ7UCnIigANgWO9fd-eKsoangN0tNxdLR39woIIkYqaud4u_ZfgrKUboSTZwfTEuA58E9WT34BMKoh8bMK6bgj4k4cTYhaVfAWEYCrPHxlf1zFkFlMyIqzP6hWYDX3lacNygy_BPrIpLtUo5aM8ix3BpCJqVjf1hQIKDBydKoYH3fWgHV0o=", api_id=API_ID, api_hash=API_HASH)


@app.on_message(filters.command(["run", "approve"], prefixes=[".", "/"]))
async def approve(client, message):
    chat_id = message.chat.id
    await message.delete()

    while True:
        try:
            # Use async generator to fetch join requests
            async for request in client.get_chat_join_requests(chat_id):
                try:
                    user_id = request.user.id
                    await client.approve_chat_join_request(chat_id, user_id)
                    logging.info(f"Approved: {user_id}")
                    await asyncio.sleep(0.5)  # Delay to avoid hitting API limits
                except PeerIdInvalid:
                    logging.error(f"Invalid peer ID for user ID: {user_id}, skipping.")
                except FloodWait as e:
                    logging.warning(f"FloodWait encountered: Sleeping for {e.x} seconds.")
                    await asyncio.sleep(e.x)
                except RPCError as e:
                    if "USER_CHANNELS_TOO_MUCH" in str(e):
                        logging.warning(f"User {user_id} has too many channels. Skipping.")
                    else:
                        logging.error(f"Unexpected RPCError: {e}")

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            await asyncio.sleep(10)  # Sleep before retrying

    # Notify admin when loop exits (this should not happen ideally)
    msg = await client.send_message(chat_id, "**Task Stopped Unexpectedly** ⚠️")
    await asyncio.sleep(5)
    await msg.delete()


logging.info("Bot Started...")
app.run()
