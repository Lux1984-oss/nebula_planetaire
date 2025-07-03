import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 155)

try:
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_FR-CA_Denise_11.0')
except:
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0')

message = "Test vocal. Si tu m'entends, ma voix est active."
print("✅ Message envoyé à la voix : ", message)
engine.say(message)
engine.runAndWait()
