from transformers import GPT2LMHeadModel, GPT2Tokenizer
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Загрузка модели и токенизатора
model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Функция для генерации текста
def generate_text(prompt):
   inputs = tokenizer.encode(prompt, return_tensors='pt')
   outputs = model.generate(inputs, max_length=150, num_return_sequences=1)
   return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Обработка сообщений
def respond(update: Update, context: CallbackContext):
   user_message = update.message.text
   response = generate_text(user_message)
   update.message.reply_text(response)

# Основная функция
def main():
   updater = Updater("7294924577:AAHGkVHBnk2uEB0e4X3sigMJB-gHZTIQE20", use_context=True)
   dp = updater.dispatcher

   dp.add_handler(MessageHandler(Filters.text & ~Filters.command, respond))

   updater.start_polling()
   updater.idle()

if __name__ == '__main__':
   main()