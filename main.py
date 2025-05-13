
import asyncio
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = os.getenv("7403324708:AAG76th51acm-Ffe4QZtDuBjpFW34WaDBUc")  # Only the token is needed now

async def delete_soon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    message_id = update.message.message_id

    # Ignore if it's not a channel
    if update.effective_chat.type == "channel":
        await asyncio.sleep(30)  # Delay before deleting
        try:
            await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
        except Exception as e:
            print(f"Failed to delete message in {chat_id}: {e}")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, delete_soon))
    print("Bot is running...")
    await app.run_polling()

if __name__ == '__main__':
    asyncio.run(main())
