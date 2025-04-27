# chatbot_translator_speaker.py

import tkinter as tk
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
from playsound import playsound

class TranslatorChatbot:
    def _init_(self, master):
        self.master = master
        master.title("Translator and Speaker Bot")

        self.label_text = tk.Label(master, text="Enter Text:")
        self.label_text.pack()
        self.entry_text = tk.Entry(master, width=50)
        self.entry_text.pack()

        self.label_lang = tk.Label(master, text="Enter Target Language Code (e.g., 'fr' for French, 'hi' for Hindi):")
        self.label_lang.pack()
        self.entry_lang = tk.Entry(master, width=20)
        self.entry_lang.pack()

        self.chat_area = tk.Text(master, height=20, width=60)
        self.chat_area.pack()

        self.send_button = tk.Button(master, text="Translate & Speak", command=self.translate_and_speak)
        self.send_button.pack()

    def translate_and_speak(self):
        text = self.entry_text.get()
        target_lang = self.entry_lang.get()

        if not text or not target_lang:
            self.chat_area.insert(tk.END, "Bot: Please provide both text and target language code.\n")
            return

        try:
            # Translate using deep_translator
            translated_text = GoogleTranslator(source='auto', target=target_lang).translate(text)

            self.chat_area.insert(tk.END, f"You: {text}\n")
            self.chat_area.insert(tk.END, f"Bot (translated): {translated_text}\n")

            # Convert to speech
            tts = gTTS(translated_text, lang=target_lang)
            audio_file = "translated_audio.mp3"
            tts.save(audio_file)
            playsound(audio_file)
            os.remove(audio_file)

        except Exception as e:
            self.chat_area.insert(tk.END, f"Bot: Error - {str(e)}\n")

if _name_ == "_main_":
    root = tk.Tk()
    app = TranslatorChatbot(root)
    root.mainloop()