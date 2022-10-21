import constants as keys
from telegram.ext import *
import responses as r
import logging
import os
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = 'keys'

print("הבוט פעיל")

def startCommand(update, context):
    update.message.reply_text('יש לשלוח את ההודעה הבאה : תפריט או הזמנה כדי להמשיך')

def helpCommand(update, context):
    update.message.reply_text('@WeDoWeDoo')

def handleMessage(update, context):

    text = str(update.message.text).lower()



    # Bot response
    response = r.sampleResponse(text)

    update.message.reply_text(response)

def error(update, context):

    # print errors
    print(f"Update {update} cause error {context.error}")


# Run the programme
def main():
    updater = Updater(keys.API_Token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler("start", startCommand))
    dp.add_handler(CommandHandler("help", helpCommand))




    # Messages
    dp.add_handler(MessageHandler(Filters.text, handleMessage))

    dp.add_error_handler(error)


    # Run the bot
    updater.idle()
    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://intense-escarpment-48006.herokuapp.com/' + TOKEN)


main()


