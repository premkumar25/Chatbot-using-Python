from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#Give any name for your chatbot
bot = ChatBot('Jarvis')
trainer = ListTrainer(bot)

# Read the files in the chatbot corpus
#Enter the location of the chatbot_corpus
for files in os.listdir('C:/Users/prem\PycharmProjects\Chatbot\chatterbot-corpus-master\chatterbot_corpus\data\english/'):

    #open the corpus files and train the data in corpus
    data = open('C:/Users/prem\PycharmProjects\Chatbot\chatterbot-corpus-master\chatterbot_corpus\data\english/'+files,
                'r').readlines()
    trainer.train(data)

while True:

    #Get the message from the user and display the corresponding response
    user_message = input('You: ')
    if user_message.strip().lower() != 'bye':
        reply = bot.get_response(user_message)
        print('Jarvis: ', reply)
    else:
        print('Jarvis: ', 'Bye')
        break
