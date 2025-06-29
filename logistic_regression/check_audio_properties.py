import librosa

audio, sr = librosa.load('data/original/en03_sherry.wav', sr=None)
print(f"Sample Rate: {sr} Hz")
