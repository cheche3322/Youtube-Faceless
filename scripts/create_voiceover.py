import pyttsx3

def create_voiceover(script, output_file):
    engine = pyttsx3.init()
    engine.save_to_file(script, output_file)
    engine.runAndWait()

if __name__ == "__main__":
    script = "Sample script for voiceover creation."
    create_voiceover(script, "output.mp3")
