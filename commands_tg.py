from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, CallbackContext
from user_preferences import user_preferences


# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Привет! Ты можешь задать любой вопрос, на русском или английском языке. Текстом или голосом.')

async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("English", callback_data='EN'),
            InlineKeyboardButton("Russian", callback_data='RU'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Для общения с ботом голосом выберите язык', reply_markup=reply_markup)

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query

    await query.answer()
    user_id = update.effective_user.id

    if query.data == 'EN':
        context.user_data['language'] = 'EN'
        user_preferences[user_id] = 'en-GB'
        await query.edit_message_text(text='Language selected: English')
    elif query.data == 'RU':
        context.user_data['language'] = 'RU'
        user_preferences[user_id] = 'ru'
        await query.edit_message_text(text='Выбранный язык: Русский')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Этот бот умеет отвечать текстом на вопросы, заданные текстом и голосом на английском и русском языках. Для начала работы выберите язык голосовых сообщений в меню')