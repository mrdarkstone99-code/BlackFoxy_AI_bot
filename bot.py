from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from config import BOT_TOKEN
from ai.brain import generate_reply
from utils.translator import smart_translate


# START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 BlackFoxy AI Online\n\n"
        "Commands:\n"
        "/translate text | lang\n"
        "/chatmode (normal chat)\n"
        "/whatsapp text | lang\n"
    )


# NORMAL CHAT
async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    reply = generate_reply(text)
    await update.message.reply_text(reply)


# FORMAL TRANSLATE
async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)

    if "|" in text:
        msg, lang = text.split("|", 1)
        result = smart_translate(msg.strip(), lang.strip(), mode="formal")
        await update.message.reply_text(result)
    else:
        await update.message.reply_text("Use: /translate hello | fr")


# WHATSAPP STYLE TRANSLATE
async def whatsapp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = " ".join(context.args)

    if "|" in text:
        msg, lang = text.split("|", 1)
        result = smart_translate(msg.strip(), lang.strip(), mode="chat")
        await update.message.reply_text(result)
    else:
        await update.message.reply_text("Use: /whatsapp hello | fr")


# BOT SETUP
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("translate", translate))
app.add_handler(CommandHandler("whatsapp", whatsapp))

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, chat)
)

print("BlackFoxy AI Running...")

app.run_polling()
