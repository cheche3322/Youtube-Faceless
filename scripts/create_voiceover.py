from TTS.api import TTS

def create_voiceover(text, output_path):
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
    tts.tts_to_file(text=text, file_path=output_path)

if __name__ == "__main__":
    text = "This is a test voiceover generated using Coqui TTS."
    output_path = "static/thumbnails/voiceover.wav"
    create_voiceover(text, output_path)
