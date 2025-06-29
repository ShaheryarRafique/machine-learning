import os
import librosa
import soundfile as sf

# Set your paths
input_folder = 'data/original'      
output_folder = 'data/resampled'    

# Make output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop over all .wav files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.wav'):
        file_path = os.path.join(input_folder, filename)
        
        # Load audio with original sampling rate
        audio, sr = librosa.load(file_path, sr=None)
        
        # Resample to 16kHz
        audio_16k = librosa.resample(audio, orig_sr=sr, target_sr=16000)
        
        # Save resampled audio to output folder
        output_path = os.path.join(output_folder, filename)
        sf.write(output_path, audio_16k, 16000)
        
        print(f"Resampled {filename} from {sr}Hz to 16kHz")
