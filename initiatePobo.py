# import speech_recognition as sr

# r = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Speak anything: ")
#     audio = r.listen(source)

#     try:
#         text = r.recognize_google(audio)
#         print('You said: {}'.format(text))
#     except:
#         print('Sorry could not recognize your voice')

from chatbotBrain.nltkCustomChatUtilModule import Chat, reflections
from chatbotBrain.reflectionsModule import pairs
import random
import time
from chatbotBrain.ipFinderModule import getCityFromIP

from os import system, name

def clear():
    if name == 'nt': 
        _ = system('cls')
    else: 
        _ = system('clear')

def initiatePobo():
    clear()
    print("initializing chatbot...")
    time.sleep(2)
    print("\n\n\nPobo >> Hi, I'm Pobo. Ask me anything. :)")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    initiatePobo()
    print("\n\n\n\n\n")
    system("pause...")