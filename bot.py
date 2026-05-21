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
from utils.translator import translate_text


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 BlackFoxy AI Online\n\n"
        "Commands:\n"
        "/translate hello | fr\n"
        "Chat normally with me 🤖"
    )


async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = " ".join(context.args)

    if "|" in text:
        msg, lang = text.split("|", 1)

        result = translate_text(
            msg.strip(),
            lang.strip()
        )

        await update.message.reply_text(result)

    else:
        await update.message.reply_text(
            "Use: /translate hello | fr"
        )


async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_text = update.message.text

    response = generate_reply(user_text)

    await update.message.reply_text(response)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("translate", translate))
app.add_handler(
    MessageHandler(
        filters.TEXT & ~filters.COMMAND,
        chat
    )
)

print("BlackFoxy AI Started")

app.run_polling()
