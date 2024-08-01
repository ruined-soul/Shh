from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Replace 'YOUR_TOKEN' with your bot's API token
TOKEN = '7244701752:AAErthlFv4llgquDNHkUSWCbX-YZhPP_iKA'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! I am your echo bot. Send me any message, and I will echo it back.')

async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(update.message.text)

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling()

if __name__ == '__main__':
    main()
