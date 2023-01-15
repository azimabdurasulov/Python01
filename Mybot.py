from telegram.ext import Updater,CommandHandler,CallbackContext,MessageHandler,Filters,CallbackQueryHandler
from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton
import os

# get token from env
TOKEN = os.environ['TOKEN']



def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['🛍 Shop','📦 Cart'],
        ['📞 Contact','📝 About']
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )

def about(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = ReplyKeyboardMarkup([
        ['📝 About Us','📝 About the bot'],
        ['Main menu']
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )

def contact(update: Update, context: CallbackContext):
    chat_id = update.message.chat.id

    keyboar = InlineKeyboardMarkup([
        [InlineKeyboardButton(text='📞 Phone number',callback_data='number')],
        # [InlineKeyboardButton(text='📞 Phone number',url='txt')]
        
    ])
    bot = context.bot
    bot.sendMessage(
    chat_id=chat_id,
    text='Assalom alaykum xush kelibsiz botimizga 👍',
    reply_markup=keyboar
    )

def query(update: Update, context: CallbackContext):
    print('Query')
    pass

def menyu(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    keyboar = ReplyKeyboardMarkup([
        ['Boshlash','📝 Davom etish'],
        ['O\'qigan it']
    ])
    bot = context.bot
    bot.sendMessage(
        chat_id=chat_id,
        text="📝 Menyularimizni kurib chiqing 👍",
        reply_markup=keyboar
    )

def dog(update: Update, context:CallbackContext):
    chat_id=update.message.chat_id

    keyboar = ReplyKeyboardMarkup([
        ["🛑 Bosh sahifaga o\'tish"]
    ])
    bot = context.bot
    bot.sendPhoto(
        chat_id=chat_id,
        photo="https://random.dog/2bff25d0-c721-4078-8cc9-f3ce6b464428.jpg",
        reply_markup = keyboar
    )



updater = Updater(token=TOKEN)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📝 About'),about))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📞 Contact'),contact))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Main menu'),menyu))
updater.dispatcher.add_handler(MessageHandler(Filters.text('O\'qigan it'),dog))
updater.dispatcher.add_handler(MessageHandler(Filters.text("🛑 Bosh sahifaga o\'tish"),start))

updater.start_polling()
updater.idle()