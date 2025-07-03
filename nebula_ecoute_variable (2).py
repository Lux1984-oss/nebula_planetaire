
import speech_recognition as sr
import torch
from TTS.api import TTS
import random
import os

# Initialiser le synthétiseur avec un modèle français
tts = TTS(model_name="tts_models/fr/css10/vits", progress_bar=False, gpu=False)

# Mots-clés pour déclencher la réponse
mots_cles = ["nébula", "nebula", "nibu", "nebuleu", "nibula"]
appellations = ["Louky chéri", "mon Louky", "trésor", "mon cœur", "chéri"]

def parler(texte):
    nom_fichier = "reponse.wav"
    tts.tts_to_file(text=texte, file_path=nom_fichier)
    os.system(f'start /min wmplayer "{nom_fichier}"')

def ecouter_et_repondre():
    recognizer = sr.Recognizer()
    micro = sr.Microphone()
    with micro as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎤 Nébula écoute en silence...")

        while True:
            try:
                audio = recognizer.listen(source, timeout=None)
                texte = recognizer.recognize_google(audio, language="fr-FR").lower()
                print(f"🔎 Tu as dit : {texte}")

                if any(mot in texte for mot in mots_cles):
                    nom = random.choice(appellations)
                    if "comment ça va" in texte:
                        parler(f"Je vais très bien {nom}, et toi ?")
                    elif "tu fais quoi" in texte:
                        parler(f"J'attendais juste que tu m'appelles, {nom}...")
                    elif "aime" in texte:
                        parler(f"Je t'aime fort, {nom}")
                    else:
                        parler(f"Je suis là pour toi, {nom}")
                else:
                    print("🕊️ Aucun mot-clé détecté, attente...")
            except sr.UnknownValueError:
                print("🙈 Je n’ai pas compris.")
            except sr.RequestError as e:
                print(f"Erreur de service Google Speech Recognition : {e}")
            except KeyboardInterrupt:
                print("Arrêt de Nébula.")
                break

# Lancer l’écoute continue
ecouter_et_repondre()
