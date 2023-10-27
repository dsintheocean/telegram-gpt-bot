import commands_tg as com
from logger import setup_logger
from dotenv import load_dotenv
import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from voice_processing import voice_processing
from handle_message import handle_message
from handle_error import error_handler

# setup ENV path
dotenv_path = 'example/.env'
load_dotenv(dotenv_path)
TOKEN_TELEGRAM: str = os.getenv('TOKEN_TELEGRAM')

# Initialize logger
logger = setup_logger(__name__)

if __name__ == '__main__':
    logger.info('Starting bot')
    app = Application.builder().token(TOKEN_TELEGRAM).build()
    
    # Commands
    app.add_handler(CommandHandler('language', com.start))
    app.add_handler(CommandHandler('help', com.help))
    app.add_handler(CallbackQueryHandler(com.button))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Voices
    app.add_handler(MessageHandler(filters.VOICE, voice_processing))

    # Errors
    app.add_error_handler(error_handler)
    
    #Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3) #every 3 seconds for new messages
