import logging
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait, PeerIdInvalid, RPCError

logging.basicConfig(level=logging.ERROR)

API_ID = 24323145  # Replace with your API ID
API_HASH = "2255461d65e3ad2440a936bc078b301f"  # Replace with your API hash

app = Client("user_account_session", api_id=API_ID, api_hash=API_HASH)


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
