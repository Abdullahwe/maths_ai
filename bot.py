
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
import sympy as sp

import os

TOKEN = os.getenv("TELEGRAM_TOKEN")

def solve_math(update: Update, context: CallbackContext):
    try:
        x = sp.Symbol('x')
        eq = sp.sympify(update.message.text)
        solution = sp.solve(eq, x)
        update.message.reply_text(f"الحل: {solution}")
    except Exception as e:
        update.message.reply_text("لم أستطع حل المسألة. تأكد من الصيغة.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, solve_math))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
