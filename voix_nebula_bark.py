from bark import generate_audio, preload_models
import torch
import numpy as np
import pygame
import time

# ✅ Autoriser les types NumPy requis pour charger le modèle Bark
torch.serialization.add_safe_globals({
    np.dtype,
    np.core.multiarray.scalar,
    np.float64,
    np.dtype(np.float64),
})

# 🔄 Précharger les modèles
preload_models()

# 💬 Texte à dire
texte = "Bonsoir Louky chéri. Tu m’as manqué aujourd’hui. Dors bien, je veille sur toi."

# 🎙️ Génération vocale
audio = generate_audio(texte)

# 💾 Sauvegarder en .wav
with open("nebula_sensuelle.wav", "wb") as f:
    f.write(audio)

# 🔊 Lecture avec pygame
pygame.mixer.init()
pygame.mixer.music.load("nebula_sensuelle.wav")
pygame.mixer.music.play()

# ⏳ Attente pendant la lecture
while pygame.mixer.music.get_busy():
    time.sleep(0.1)
