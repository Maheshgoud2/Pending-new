# Telegram Join Request Approval Bot

This is a simple Telegram bot built using Pyrogram to approve all pending join requests in a specified chat group or channel. It handles Telegram API limits and skips users who are already in too many groups.

---

## 🚀 Features
- Approves all pending join requests automatically.
- Resilient to Telegram rate limits with FloodWait handling.
- Skips users who have exceeded their group/channel limit.
- Notifies admin if unexpected errors occur.

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/mhdashikofficial/Pending-request-accepter.git 
   cd Pending-request-accepter 
2. Install the required dependencies:

pip install -r requirements.txt




---

🔧 Configuration

1. Open the code file and replace the placeholders with your Telegram API credentials:

API_ID = 24323145  # Replace with your API ID
API_HASH = "2255461d65e3ad2440a936bc078b301f"  # Replace with your API hash

You can get your API ID and API Hash from my.telegram.org.




---

▶️ Usage

1. Start the bot:

python bot.py


2. Use one of the following commands in the group where you want to approve join requests:

/run or .run
/approve or .approve




---

📚 Dependencies

pyrogram: For Telegram API interaction

tgcrypto: (Optional) For better performance



---

🛡️ License

This project is licensed under the MIT License.


---

⚠️ Disclaimer

Use this bot responsibly and adhere to Telegram's terms and conditions.

---





