from response_gpt import gpt_response as resp_gpt
from logger import setup_logger
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes

# setup ENV path
dotenv_path = '/Users/mi_xzm/vscode/python/.venv/.env'
load_dotenv(dotenv_path)
BOT_USERNAME: str = os.getenv('BOT_USERNAME')

# Initialize logger
logger = setup_logger(__name__)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type # inform whether it's group chat or private chat
    text: str = update.message.text
    logger.info(f'User({update.message.chat.id}): "{text}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = resp_gpt(new_text)
        else:
            return
    else:
        response: str = resp_gpt(text)
    await update.message.reply_text(response)