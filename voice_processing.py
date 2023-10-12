import speech_recognition as sr
from pydub import AudioSegment
import os
from telegram import Update
from telegram.ext import ContextTypes
from response_gpt import gpt_response as resp_gpt
from user_preferences import user_preferences

FILE_PATH = '/Users/mi_xzm/vscode/python/.venv/'

def convert_oga_to_wav(oga_file_path, wav_file_path):
    audio = AudioSegment.from_file(oga_file_path, format='ogg')
    audio.export(wav_file_path, format='wav')

def transcribe_wav_to_text(wav_file_path, user_id):
    recognizer = sr.Recognizer()
    
    if user_id in user_preferences:
        language = user_preferences[user_id]
    
    with sr.AudioFile(wav_file_path) as audio_file:
        audio_data = recognizer.record(audio_file)
        text = recognizer.recognize_google(audio_data, language=language) #ru or en-GB
        return text
    
async def voice_processing(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file_id: str = update.message.voice.file_id
    oga_file_path = os.path.join(FILE_PATH,file_id+'.wav')
    wav_file_path = os.path.join(FILE_PATH,file_id+'.oga')
    
    new_file = await context.bot.get_file(file_id)
    await new_file.download_to_drive(oga_file_path)
    convert_oga_to_wav(oga_file_path, wav_file_path)
    text = transcribe_wav_to_text(wav_file_path, update.effective_user.id)
    if update.effective_user.id in user_preferences:
        language = user_preferences[update.effective_user.id]
        if language == 'ru':
            await update.message.reply_text(f'Ваш текст был распознан как: "{text}"')
        elif language == 'en-GB':
            await update.message.reply_text(f'Your text was transcribed as: "{text}"')
        else:
            await update.message.reply_text(f'Ваш текст был распознан как: "{text}"')
    os.remove(oga_file_path)
    os.remove(wav_file_path)
    response: str = resp_gpt(text)
    await update.message.reply_text(response)