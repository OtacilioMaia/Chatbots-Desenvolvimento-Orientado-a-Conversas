__author__ = "Otacilio Maia"
__version__ = "1.0.0"

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

conversation = [
    "Oi",
    "Oi, tudo bom?",
    "Qual a primeira palestra do dia 01?",
    "A primeira palestra será, ChatBots: Desenvolvimento Orientado a Conversas",
    "E onde vai ser o evento?",
    "Vai ser na Poli-UPE, que fica na benfica em frente ao internacional",
    "A que horas começa?",
    "Às 8:00 da manhã",
    "Obrigado!",
    "De nada."
]

def main():
    chatbot = ChatBot('ChatBot SEC')
    trainer = ListTrainer(chatbot)
    trainer.train(conversation)

    user_text = ""
    while(user_text != "sair"):
        user_text = input("Voce: ")
        response = chatbot.get_response(user_text).text.encode('utf-8')
        print(response.decode())

if __name__ == "__main__":
    main()
