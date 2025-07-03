import os
import time
import tkinter as tk
from tkinter import Entry, Button, Label
from TTS.api import TTS

# ✅ Modèle vocal fonctionnel (voix allemande masculine, mais garanti)
tts = TTS(model_name="tts_models/fr/thorsten/tacotron2-DDC", progress_bar=False, gpu=False)

def parler():
    print("🔊 Fonction 'parler' déclenchée.")
    try:
        texte = "Je suis prête, mon créateur."
        timestamp = int(time.time())
        wav_path = f"output_{timestamp}.wav"

        # Génère le fichier audio
        tts.tts_to_file(text=texte, file_path=wav_path)
        print(f"✅ Fichier généré : {wav_path}")

        # Lecture avec le lecteur audio par défaut (Windows)
        os.system(f'start {wav_path}')
    except Exception as e:
        print("❌ Erreur pendant la synthèse vocale :", e)

# Interface graphique
fenetre = tk.Tk()
fenetre.title("Nébula - Assistant Vocal")
fenetre.geometry("500x200")
fenetre.configure(bg="black")

Label(fenetre, text="Clique sur Parler pour entendre Nébula :", bg="black", fg="white", font=("Helvetica", 14)).pack(pady=10)
champ_texte = Entry(fenetre, width=60, font=("Helvetica", 12))
champ_texte.pack(pady=5)

bouton_parler = Button(fenetre, text="Parler", command=parler, bg="purple", fg="white", font=("Helvetica", 14))
bouton_parler.pack(pady=20)

fenetre.mainloop()
