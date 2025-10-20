from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime
import os

TOKEN = os.environ.get('TELEGRAM_TOKEN', '8207855982:AAEJJNujQYD4ekek7VqQLP5DlDYA9JOByVY')
ADMIN_ID = 6152409314

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    # اطلاع به مدیر
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"👤 کاربر جدید وارد ربات شد:\n\n"
             f"• نام: {user.first_name or 'ناشناس'}\n"
             f"• یوزرنیم: @{user.username or 'ندارد'}\n"
             f"• زمان: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
             f"• اقدام: شروع ربات"
    )
    
    # پاسخ به کاربر
    await update.message.reply_text(
        "👋 سلام! به فروشگاه شایلا خوش آمدید\n\n"
        "📝 برای ثبت سفارش از /order استفاده کنید\n"
        "🛍️ برای محصولات از /products استفاده کنید"
    )

async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"🛒 کاربر درخواست ثبت سفارش کرد:\n\n"
             f"• نام: {user.first_name or 'ناشناس'}\n"
             f"• زمان: {datetime.now().strftime('%H:%M:%S')}"
    )
    
    await update.message.reply_text(
        "📝 برای ثبت سفارش به لینک زیر بروید:\n\n"
        "🔗 https://docs.google.com/forms/d/e/1FAIpQLSfkz8yJ4mdZ51-Sr62KiHd6fRbgNK7xlNh0NBSRRb_rYRGw7Q/viewform"
    )

print("✅ ربات فروشگاه شایلا راه‌اندازی شد!")
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("order", order))
app.run_polling()
