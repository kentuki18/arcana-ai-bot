from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8922234866:AAHuJP2pnK_w4V_dXJTCQcCCGKieq8j5nAU"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔮 Arcana AI Bot работает!")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
