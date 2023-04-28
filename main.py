import pyttsx3
import pandas as pd
import datetime as dt
import random

class ChatBot:
    def __init__(self):
        self.keywords = []
        self.responses = []
        self.greetings = ["¿Qué pasa?" , "¡Hola!" , "¡Saludos!"]
        self.goodbyes = ["¡Adiós!" , "¡Hasta luego!" , "¡Nos vemos pronto!"]
    def brain(self):
        df = pd.read_csv("data/data.csv")
        brain = df.dropna()
        date = dt.datetime.now().strftime("%d-%m-%y")
        csvName = "data/data" + str(date) + ".csv"
        brain.to_csv(csvName)
        self.keywords = brain['keywords'].values.tolist()
        self.responses = brain['responses'].values.tolist()
    #Convert text to speech
    def speakText(self , command):
        #Engine
        engine = pyttsx3.init()
        engine.say(command)
        engine.runAndWait()
    def userInput (self):
        gt = random.choice(self.greetings)
        print(gt)
        self.speakText(gt)

        user = input("Escribe algo (o escribe 'adios' para salir): ")
        user = user.lower()

        while (user != "bye"):
            keyword_found = False

            for index in range(len(self.keywords)):
                if (self.keywords[index] in user):
                    print("Bot: " + self.responses[index])
                    self.speakText(self.responses[index])
                    keyword_found = True

            if (keyword_found == False):
                print("Aprendiendo...")
                print("No estoy seguro de cómo responder")
                self.newKeyword = user
                self.keywords.append(self.newKeyword)
                print("¿Cómo puedo responder a " + self.newKeyword + "?")
                self.newResponse = input("User: ")
                self.responses.append(self.newResponse)

                data = { 'keywords' : [self.newKeyword] , 'responses' : [self.newResponse] }
                dataLoad = pd.DataFrame(data)

                dataLoad.to_csv('data/data.csv', mode='a', index=False, header=False)

            user = input("Escribe algo (o escribe 'adios' para salir): ")
            user = user.lower()
        
        gb = random.choice(self.goodbyes)
        print(gb)
        self.speakText(gb)

bot = ChatBot()
bot.brain()
bot.userInput()