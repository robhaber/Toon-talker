import pyttsx3
from gtts import gTTS
import librosa


def txt_to_male(text, voice_path):
    txt_to_female(text, voice_path)
    y, sr = librosa.load(voice_path, sr=16000)
    y_shifted = librosa.effects.pitch_shift(y, sr, n_steps=-4) 
    librosa.output.write_wav(voice_path, y_shifted, sr)


def txt_to_female(text, voice_path):
    language = 'en' 
    speech = gTTS(text = text, lang = language, slow = False)
    speech.save(voice_path)





