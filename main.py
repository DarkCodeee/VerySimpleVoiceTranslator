from googletrans import Translator, constants
from pynput import keyboard

import speech_recognition as s_r
import json

with open("config.json", encoding="utf-8") as f:
    config = json.load(f)

with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.KeyCode(char=config.get("button_activate")) and str(event.__class__.__name__) == "Press":
            try:
                r = s_r.Recognizer()
                my_mic = s_r.Microphone(device_index=1)
                with my_mic as source:
                    print("Say now!!!!")
                    audio = r.listen(source)
                text = r.recognize_google(audio, language=config.get("native_lang"))

                translator = Translator()


                translation = translator.translate(text, dest=config.get("translate_lang"))
                print(">>>", text)
                print(f"{translation.text} ({translation.dest})\n")
            except Exception as e:
                print("ошибка ->", e)