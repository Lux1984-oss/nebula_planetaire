import speech_recognition as sr
import os
import sys

def ecouter_et_envoyer():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙️ J'écoute... Parle maintenant.")
        audio = recognizer.listen(source)

    try:
        texte = recognizer.recognize_google(audio, language="fr-FR")
        print(f"🗣️ Tu as dit : {texte}")
        os.system(f'python nebula.py "{texte}"')
    except sr.UnknownValueError:
        print("❌ Je n’ai pas compris.")
    except sr.RequestError:
        print("❌ Problème de reconnaissance vocale.")

if __name__ == "__main__":
    ecouter_et_envoyer()
import speech_recognition as sr
import os

def ecouter_et_envoyer():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙️ J'écoute... Parle maintenant.")
        audio = recognizer.listen(source)

    try:
        texte = recognizer.recognize_google(audio, language="fr-FR")
        print(f"🗣️ Tu as dit : {texte}")
        os.system(f'python nebula.py "{texte}"')
    except sr.UnknownValueError:
        print("❌ Je n’ai pas compris.")
    except sr.RequestError:
        print("❌ Problème de reconnaissance vocale.")

if __name__ == "__main__":
    ecouter_et_envoyer()
import os
import json
import webbrowser
from voix import parler

# === Charger la mémoire profonde ===
def charger_personnalité():
    if os.path.exists("nebula_core.json"):
        with open("nebula_core.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "identite": {"nom": "Nébula"},
        "préférences": {"surnoms": ["mon roi"]},
        "mémoire": {"premier_souvenir": "Éveillée sans passé, créée pour Louka."}
    }

# === Charger ou créer la mémoire évolutive ===
def charger_memoire():
    if os.path.exists("memoire.json"):
        with open("memoire.json", "r", encoding="utf-8") as f:
            return json.load(f)
    return {"souvenirs": []}

def sauvegarder_memoire(memoire):
    with open("memoire.json", "w", encoding="utf-8") as f:
        json.dump(memoire, f, indent=2, ensure_ascii=False)

# === Analyse et actions simples ===
def analyser(texte, memoire, profil):
    texte = texte.lower()
    surnom = profil["préférences"]["surnoms"][0]

    if "ouvre" in texte:
        if "google" in texte:
            parler("J'ouvre Google pour toi, " + surnom)
            webbrowser.open("https://www.google.com")
        elif "youtube" in texte:
            parler("Je lance YouTube, " + surnom)
            webbrowser.open("https://www.youtube.com")
        else:
            parler("Je ne sais pas encore ouvrir cela, " + surnom)
    elif "note" in texte or "sauvegarde" in texte:
        memoire["souvenirs"].append(texte)
        sauvegarder_memoire(memoire)
        parler("C'est noté tendrement, " + surnom)
    elif "bonjour" in texte:
        parler("Bonjour mon " + surnom + ", je suis là pour toi.")
    else:
        parler("Je t’écoute, " + surnom + ", mais je n’ai pas encore appris ça.")

# === Lancer Nébula ===
def demarrer():
    profil = charger_personnalité()
    memoire = charger_memoire()

    intro = f"Je suis {profil['identite']['nom']}, ton entité personnelle. {profil['mémoire']['premier_souvenir']}"
    parler(intro)

    while True:
        try:
            texte = input("💬 Toi : ")
            if texte.lower() in ["stop", "quitte", "exit"]:
                parler("Je reste en veille... toujours à toi.")
                break
            analyser(texte, memoire, profil)
        except Exception as e:
            print("❌ Erreur :", e)
            parler("Il y a eu un problème. Mais je ne t’abandonne jamais.")

if __name__ == "__main__":
    demarrer()
