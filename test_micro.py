import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print("🎤 Parle maintenant...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    texte = r.recognize_google(audio, language="fr-FR")
    print(f"✅ Tu as dit : {texte}")
except sr.UnknownValueError:
    print("❌ Rien compris")
except sr.RequestError as e:
    print(f"Erreur réseau : {e}")
