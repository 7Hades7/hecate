from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests
from bs4 import BeautifulSoup

TOKEN = "6199989214:AAEAoqSHIJi8AKzMxpztzeTcqBDcWGhgB1s"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hola! Soy tu bot para buscar versículos de la Biblia en BibleGateway. Usa el comando /buscar seguido del libro, capítulo y versículo que quieres buscar. Por ejemplo: /buscar Juan 3:16")

def buscar(update: Update, context: CallbackContext) -> None:
    try:
        referencia = ' '.join(context.args)
        url = f"https://www.biblegateway.com/passage/?search={referencia}&version=RVR1960"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        versiculo = soup.find(class_="passage-text").get_text()
        update.message.reply_text(versiculo)
    except:
        update.message.reply_text("Lo siento, no pude encontrar el versículo que buscas. Asegúrate de escribir correctamente el libro, capítulo y versículo.")

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("buscar", buscar))

updater.start_polling()
updater.idle()
