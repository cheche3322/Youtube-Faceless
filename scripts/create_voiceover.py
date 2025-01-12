from gtts import gTTS
import os

def create_voiceover(script, output_file):
    tts = gTTS(text=script, lang='en')
    tts.save(output_file)

if __name__ == "__main__":
    script = "Sample script for voiceover creation."
    create_voiceover(script, "output.mp3")
