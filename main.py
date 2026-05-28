from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8357281606:AAHjYWWzgjTDEYTk3aLHwjvRnXxGPU8FJz0"

keyboard = [
    ["⚡ Fast Keno", "🎰 Bingo"],
    ["🐔 Chicken", "👤 Avatar"]
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🔥 Welcome to Hameruha Games",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("🔥 Bot Running...")

app.run_polling()
