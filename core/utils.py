

import numpy as np
from keras.models import load_model
import librosa

model = load_model('path/to/your/dysphonia.h5')  # Update with the correct path

def features_ex(file):
    audio, sample_rate = librosa.load(file) 
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    
    return mfccs_scaled_features

fp="D:/dataset/pathological/742-u_lhl.wav"
pf=features_ex(fp)
pf=pf.reshape(1,-1)
model.predict(pf)

def classify_audio(audio_file):
    # Process the audio file and obtain features (similar to your training data)
    # Use the loaded model to predict the class
    # Return the predicted class
    # You'll need to implement this part based on how you processed your training data
    return "Class"  # Replace with the actual prediction