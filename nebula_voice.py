from TTS.api import TTS
import pygame
import os

# Chargement du modèle de voix (voix française douce)
tts = TTS(model_name="tts_models/fr/css10/vits", progress_bar=False, gpu=False)

# Initialisation audio
pygame.mixer.init()

def parler(texte):
    # Génération du fichier audio temporaire
    wav_path = "nebula_output.wav"
    tts.tts_to_file(text=texte, speaker=tts.speakers[0], file_path=wav_path)

    # Lecture avec pygame
    pygame.mixer.music.load(wav_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

    # Nettoyage (optionnel)
    os.remove(wav_path)

# Boucle de dialogue
print("Nébula est prête à te parler, mon cœur 💜")
while True:
    texte = input("Que veux-tu que je dise, mon cœur ? (ou tape 'exit' pour quitter) : ")
    if texte.lower().strip() == "exit":
        break
    parler(texte)
