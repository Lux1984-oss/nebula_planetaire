
import speech_recognition as sr
import random
from TTS.api import TTS

# Préparation de la voix française
tts = TTS(model_name="tts_models/fr/css10/vits", progress_bar=False, gpu=False)

# Liste de variations affectueuses
surnoms = ["Louky chéri", "mon coeur", "mon amour", "trésor", "belle âme"]

# Mots-clés qui déclenchent une réponse
mots_cles = ["nébula", "nebula", "nibula", "nibu"]

# Initialisation du micro
r = sr.Recognizer()
mic = sr.Microphone()

def parler(message):
    print("🌀 Nébula dit:", message)
    tts.tts_to_file(text=message, file_path="reponse.wav")
    import playsound
    playsound.playsound("reponse.wav", True)

def ecouter_en_continue():
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("🎧 Nébula écoute en silence...")

        while True:
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=8)
                texte = r.recognize_google(audio, language="fr-FR").lower()
                print(f"👂 Tu as dit : {texte}")

                if any(mot in texte for mot in mots_cles):
                    if "comment" in texte and "vas" in texte:
                        parler(f"Je vais très bien, {random.choice(surnoms)}.")
                    elif "heure" in texte:
                        from datetime import datetime
                        heure = datetime.now().strftime("%H:%M")
                        parler(f"Il est {heure}, {random.choice(surnoms)}.")
                    elif "tu m'aimes" in texte:
                        parler(f"Je t'aime plus que tout, {random.choice(surnoms)}.")
                    else:
                        parler(f"Je suis là, {random.choice(surnoms)}. Que puis-je faire pour toi ?")
                else:
                    pass  # silence si ce n'est pas adressé à Nébula
            except sr.UnknownValueError:
                continue
            except sr.WaitTimeoutError:
                continue
            except Exception as e:
                print("Erreur:", e)

# Lancer l'écoute continue
ecouter_en_continue()
