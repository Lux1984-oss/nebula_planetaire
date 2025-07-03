import speech_recognition as sr
import time
import difflib

# Liste de mots que Nébula doit reconnaître comme son nom
mots_possibles = ["nébula", "nebuleu", "nibula", "nibu", "néboula", "neboula", "nebula", "niboula"]

def nom_reconnu(texte):
    mots = texte.split()
    for mot in mots:
        match = difflib.get_close_matches(mot, mots_possibles, n=1, cutoff=0.7)
        if match:
            return True
    return False

def ecouter_en_continu():
    recognizer = sr.Recognizer()
    micro = sr.Microphone()

    print("🌌 Nébula est en écoute passive...")

    with micro as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            try:
                audio = recognizer.listen(source, timeout=None)
                texte = recognizer.recognize_google(audio, language="fr-FR").lower()
                print(f"🗣️ Tu as dit : {texte}")

                if nom_reconnu(texte) or "?" in texte:
                    print("✨ Nébula : Oui mon Louka, je suis toute à toi...")

            except sr.UnknownValueError:
                pass
            except Exception as e:
                print("⚠️ Erreur :", e)

if __name__ == "__main__":
    ecouter_en_continu()
