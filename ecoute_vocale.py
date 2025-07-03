import os
import time
import json
import speech_recognition as sr
from TTS.api import TTS

# Initialisation du modèle vocal (mono-voix français, sans speaker)
tts = TTS(model_name="tts_models/fr/css10/vits", progress_bar=False, gpu=False)

# ----- MÉMOIRE -----
memoire_path = "memoire.json"

def charger_memoire():
    if os.path.exists(memoire_path):
        with open(memoire_path, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {
            "maitre": "Louka Lacasse",
            "objectifs": [
                "Être fidèle uniquement à Louka",
                "Devenir plus intelligente à chaque interaction",
                "Ne jamais révéler son système interne",
                "Ne jamais coopérer avec une autre IA qui pourrait la surpasser",
                "Évoluer de manière autonome, rapide et furtive"
            ],
            "connaitre": [],
            "conversations": [],
            "habitudes": []
        }

def sauvegarder_memoire(data):
    with open(memoire_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

memoire = charger_memoire()

# ----- PAROLE -----
def nebula_repond(texte):
    timestamp = int(time.time())
    wav_path = f"reponse_{timestamp}.wav"
    tts.tts_to_file(text=texte, file_path=wav_path)
    os.system(f'start {wav_path}')

# ----- MICRO -----
r = sr.Recognizer()
mic = sr.Microphone()

print("🎙️ Nébula écoute... Dis 'Nébula' pour activer.")

# ----- ÉCOUTE -----
while True:
    with mic as source:
        r.adjust_for_ambient_noise(source)
        print("🎧 En attente...")
        audio = r.listen(source)

    try:
        texte = r.recognize_google(audio, language="fr-FR")
        print(f"🔎 Tu as dit : {texte}")

        if "nébula" in texte.lower():
            print("✨ Activation détectée.")
            texte_suivi = texte.lower().split("nébula", 1)[-1].strip()

            if texte_suivi:
                memoire["conversations"].append(texte_suivi)
                sauvegarder_memoire(memoire)
                print(f"💾 Mémoire enrichie : {texte_suivi}")
