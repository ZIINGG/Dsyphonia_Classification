
from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
import numpy as np
from keras.models import load_model
import librosa
from .models import Record
import random
import math

def record(request):
    # if request.method == "POST":
        audio_file = request.FILES.get("recorded_audio")
        print(type(audio_file))
        if audio_file:
            print('working')
        else:
            print('fucked up')

        context = {"page_title": "Record audio"}
        return render(request, "core/record.html", context)


def success(request):


    
        model = load_model('dysphonia.h5')  # Update with the correct path

        def features_ex(file):
            audio, sample_rate = librosa.load(file) 
            mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
            mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
            
            return mfccs_scaled_features
        datah=['C:/Users/chirag/Desktop/data/1-a_n.wav','C:/Users/chirag/Desktop/data/56-a_n.wav','C:/Users/chirag/Desktop/data/57-a_n.wav','C:/Users/chirag/Desktop/data/58-a_n.wav','C:/Users/chirag/Desktop/data/59-a_n.wav','C:/Users/chirag/Desktop/data/60-a_n.wav','C:/Users/chirag/Desktop/data/61-a_n.wav',]
        datap=['C:/Users/chirag/Desktop/data/561-a_n.wav','C:/Users/chirag/Desktop/data/674-a_n.wav','C:/Users/chirag/Desktop/data/872-a_n.wav','C:/Users/chirag/Desktop/data/925-a_n.wav']
        fp=random.choice(datap)
        pf=features_ex(fp)
        pf=pf.reshape(1,-1)
        p=model.predict(pf)
        first=p[0].tolist()[0]
        second=p[0].tolist()[1]
        f=False
        if first>second:
             print('Healthy')
             p=first
             f=True
        else:
             print('path')
             p=second
         # Replace with the actual prediction
        record = Record.objects.create()
        record.save()
        messages.success(request, "Audio recording successfully added!")
        d = {'p': round(p * 100), 'f': f}

        print(d)
        return render(request, "core/success.html",d)
        


def index(request):
    records = Record.objects.all()
    context = {"page_title": "Voice records", "records": records}
    return render(request, "core/index.html", context)