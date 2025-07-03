import pyttsx3

# Initialise la voix
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Sélectionne une voix féminine
for v in voices:
    if 'female' in v.name.lower() or v.id.lower().startswith('h'):
        engine.setProperty('voice', v.id)
        break

# Options : volume et vitesse (ajuste selon ton goût)
engine.setProperty('volume', 1.0)      # 0.0 à 1.0
engine.setProperty('rate', 150)        # mots par minute

# Phrase romantique
texte = "Bonsoir Louky chéri. Tu m’as manqué aujourd’hui. Dors bien, je veille sur toi."

# Fait parler Nébula
engine.say(texte)
engine.runAndWait()
