"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import time
import logging
import time
import feedparser
from telegram.ext import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Welcome Movierulz updates BOT!\nAs soon as movierulz adds new content,BOT will notify you about newly added content.')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""

    f1 = feedparser.parse('https://4movierulz.gg//feed?unit=second')
    old = f1['entries'][0]['title']
    while True:
        time.sleep(5)
        f = feedparser.parse('https://4movierulz.gg//feed?unit=second')
        new = f['entries'][0]['title']
        if old == new:
            print("same:{}={}".format(old,new))
        else:
            update.message.reply_text("New Content Added in Movierulz\nTitle:{}\nLink:{}\nPublished:{}".format(f['entries'][0]['title'],f['entries'][0]['link'],f['entries'][0]['published']))
            print("New Content Added in Movierulz")
            print("Title:", f['entries'][0]['title'])
            print("Link:", f['entries'][0]['link'])
            print("Published-On:", f['entries'][0]['published'])
            old = new
            continue


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("991345549:AAHGq7HyZWU2eGkOZs16RXLzgih65q7ZZ4Q", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
