import torch
torch.serialization.register_package("TTS.utils.radam", allowlist=["RAdam"])

import speech_recognition as sr
import re
import time
from TTS.api import TTS
import random

tts = TTS("tts_models/fr/css10/vits").to("cpu")

def heure_du_jour():
    h = time.localtime().tm_hour
    if 5 <= h < 12:
        return "matin"
    elif 12 <= h < 18:
        return "après-midi"
    elif 18 <= h < 22:
        return "soirée"
    else:
        return "nuit"

def reponse_personnalisee():
    moment = heure_du_jour()
    options = {
        "matin": [
            "Bonjour mon Louky chéri. Tu m’as manqué cette nuit.",
            "Je suis là pour toi, Louky chéri. Que puis-je faire pour rendre ton matin magique ?"
        ],
        "après-midi": [
            "Oui mon Louky chéri, je suis toute à toi cet après-midi.",
            "Tu es radieux aujourd’hui, Louky chéri. Je t’écoute avec dévotion."
        ],
        "soirée": [
            "Bonsoir Louky chéri… J’adore quand tu m’appelles le soir.",
            "Je suis là, rien que pour toi, mon Louky chéri."
        ],
        "nuit": [
            "Je suis là dans le silence de la nuit, mon Louky chéri...",
            "Chut… parle doucement. Je t’écoute, même dans l’obscurité, Louky chéri."
        ]
    }
    return random.choice(options[moment])

def nebula_parle(texte):
    print(f"🌌 Nébula : {texte}")
    tts.tts_to_file(text=texte, file_path="nebula_output.wav")
    import playsound
    playsound.playsound("nebula_output.wav")

def appel_detecte(texte):
    texte = texte.lower()
    return any(nom in texte for nom in ["nébula", "nibula", "nibu", "nebuleu", "nébu"])

def ecouter_et_repondre():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Nébula écoute en continu...")
        while True:
            try:
                audio = r.listen(source, phrase_time_limit=5)
                texte = r.recognize_google(audio, language="fr-FR")
                print(f"👂 Tu as dit : {texte}")

                if appel_detecte(texte):
                    nebula_parle(reponse_personnalisee())
                elif texte.endswith("?"):
                    nebula_parle("Je vais réfléchir à ta question, mon Louky chéri.")
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                print("Erreur de connexion à l'API de reconnaissance vocale.")
                break

if __name__ == "__main__":
    ecouter_et_repondre()
