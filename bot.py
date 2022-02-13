from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler
from secret import TOKEN
import logging

# Logging
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

# Error Debugging
def error(update: Update, context: CallbackContext):
    logging.warning('Update "%s" caused error "%s"', update, context.error)

# Start
def start(update: Update, context: CallbackContext):
    # modify text accordingly
    context.bot.send_message(chat_id = update.effective_chat.id, text = 'Hi! Click on /confess and see more!')

# Confession 
def confess(update: Update, context: CallbackContext):
    # modify text & sticker ID accordingly
    # sticker ID can be obtained from @idstickerbot on Telegram
    context.bot.send_message(chat_id = update.effective_chat.id, text = 'I have a crush on you!')
    context.bot.send_sticker(chat_id = update.effective_chat.id, sticker = 'CAACAgIAAxkBAAED5jBiB6m4JA9nItPjqJkm6xgz5cPH2AACAgADwDZPEwj1bkX6hKdZIwQ')
    
    # modify button options here
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data = 'yes'),
        InlineKeyboardButton("No", callback_data = 'no')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # modify text accordingly
    update.message.reply_text('Will you be my Valentine?', reply_markup=reply_markup)

# Confession Reply
def confession_reply(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    # ensure query.data matches the callback_data stated above
    if query.data == 'yes':
        # modify text & sticker ID accordingly
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'YAY!')
        context.bot.send_sticker(chat_id = update.effective_chat.id, sticker = 'CAACAgIAAxkBAAED5jJiB6vAmeuPLdn5gDcOyoftwPYGiQACtw8AAiY_UEpcWUV2ttCzFCME')
    else:
        # modify text & sticker ID accordingly
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'Invalid input! Please click Yes and try again!')

def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Add handlers
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(confession_reply))
    updater.dispatcher.add_handler(CommandHandler('confess', confess))

    # Error Logging
    updater.dispatcher.add_error_handler(error)


    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()

