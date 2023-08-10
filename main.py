from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton 
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

import json

# Paste your Telegram bot token here
TOKEN = "Your Telegram Bot Token: FAKSJFLAKSHFKJAHSŞDJASDKAJSD"

# main menu command
def start(update, context):
  chat_id = update.effective_chat.id
  user_id = update.effective_user.id

  keyboard = [
    [InlineKeyboardButton("Seçenek 1", callback_data='option1')],
    [InlineKeyboardButton("Seçenek 2", callback_data='option2')],
    [InlineKeyboardButton("Seçenek 3", callback_data='option3')]  
  ]

  reply_markup = InlineKeyboardMarkup(keyboard)

  context.bot.send_message(chat_id=chat_id, 
                           text="Ana menü",
                           reply_markup=reply_markup)

# Button callback handler
def button(update, context):
  query = update.callback_query

  if query.data == 'option1':
    # Actions for option 1 
    context.bot.send_message(chat_id=query.message.chat_id,
                             text="Option 1 selected!")
  
  elif query.data == 'option2': 
    # Actions for option 2  
    context.bot.send_message(chat_id=query.message.chat_id,
                             text="Option 2 selected!")
                             
  elif query.data == 'option3':
    # Actions for option 3  
    context.bot.send_message(chat_id=query.message.chat_id,
                             text="Option 3 selected!")
  
  else:
    # For unknown callback data
    context.bot.send_message(chat_id=query.message.chat_id,
                             text="Invalid selected")
  
  query.answer()

def main():
  updater = Updater(TOKEN)
  dispatcher = updater.dispatcher

  # Updater ve Dispatcher
  dispatcher.add_handler(CommandHandler('start', start))
  
  # Add button callback handler
  dispatcher.add_handler(CallbackQueryHandler(button)) 

  updater.start_polling()
  updater.idle()

if __name__ == '__main__':
  main()
