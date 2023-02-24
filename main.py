from telegram.ext import (
    MessageHandler,
    Updater,
    CommandHandler,
    CallbackContext,
    Filters
)
from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton
    )
import requests
import os
TOKEN= os.environ['TOKEN']

api_key='d9a3edbca82032cc0414c9e4f5d7e112'


def start(update: Update,context:CallbackContext):
    bot =context.bot
    chat_id =update.message.chat.id
    first_name=update.message.chat.first_name
    b1=KeyboardButton(text='Andijan')
    b2=KeyboardButton(text='Bukhara')
    b3=KeyboardButton(text='Fergana')
    b4=KeyboardButton(text='Jizzakh')
    b5=KeyboardButton(text='Urganch')
    b6=KeyboardButton(text='Namangan')
    b7=KeyboardButton(text='Navoi')
    b8=KeyboardButton(text='Qashqadaryo')
    b9=KeyboardButton(text='Samarkand')
    b10=KeyboardButton(text='Gulistan')
    b11=KeyboardButton(text='Termiz')
    b12=KeyboardButton(text='Tashkent')


    reply_markup = ReplyKeyboardMarkup([[b1,b2,b3],[b4,b5,b6],[b7,b8,b9],[b10,b11,b12]])

    bot.sendMessage(chat_id,f"{first_name} ob-xavo botga hush kelibsiz!!!", reply_markup=reply_markup)


def gradus(shahar):
    url=f'https://api.openweathermap.org/data/2.5/weather?q={shahar}&appid={api_key}'
    r=requests.get(url)
    data=r.json()
    gradus=round(data['main']['temp']-273)
    return gradus

def weather(update:Update, context: CallbackContext):
    bot =context.bot
    chat_id =update.message.chat.id
    text=update.message.text
    g = gradus(text)
    bot.sendMessage(chat_id,f'{text}: {g}°C')

updater=Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,weather))
updater.start_polling()
updater.idle()