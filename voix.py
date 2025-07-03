import pyttsx3

def parler(message):
    print("🟣 Nébula :", message)
    moteur = pyttsx3.init()
    moteur.setProperty('rate', 165)
    moteur.setProperty('volume', 0.9)
    moteur.say(message)
    moteur.runAndWait()
