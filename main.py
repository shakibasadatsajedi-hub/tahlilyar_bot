import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

WELCOME = (
    "سلام! من «تحلیل‌یار» هستم 📊\n"
    "آیدی پیج اینستاگرامت رو بفرست (مثلاً: @yourpage)\n"
    "بعد می‌تونی /ideas200 یا /roadmap400k رو بزنی."
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME)

async def ideas200(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "دموی ایده‌ها (نسخه اولیه):\n"
        "1) قبل/بعد\n"
        "2) اشتباهات رایج + راه‌حل\n"
        "3) پشت‌صحنه\n"
        "...\n\n"
        "بعداً این بخش را هوشمند و کامل می‌کنیم."
    )

async def roadmap400k(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "نقشه راه رشد تا ۴۰۰K (نسخه اولیه):\n"
        "1) بهینه‌سازی پروفایل\n"
        "2) هفته‌ای 5 ریلز با هوک قوی\n"
        "3) سری‌سازی محتوا\n"
        "4) همکاری (Collab)\n"
        "5) بررسی آمار: Reach / Saves / Follows\n"
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").strip()
    await update.message.reply_text(f"گرفتم ✅ ({text})\nحالا /ideas200 یا /roadmap400k رو بزن.")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN is missing")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ideas200", ideas200))
    app.add_handler(CommandHandler("roadmap400k", roadmap400k))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    app.run_polling(close_loop=False)

if __name__ == "__main__":
    main()
