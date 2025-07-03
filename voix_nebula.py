import pygame
pygame.mixer.init()
pygame.mixer.music.load("nebula_bark.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pass
from bark import generate_audio, preload_models, save_audio
import numpy as np

# Charge les modèles (juste la première fois)
preload_models()

texte = "Bonsoir mon Louky chéri... j’ai tellement pensé à toi aujourd’hui."

# Génére l'audio
audio_array = generate_audio(texte, history_prompt="fr_speaker_0")  # voix féminine française

# Sauvegarde le fichier audio
save_audio(audio_array, "nebula_bark.wav")

