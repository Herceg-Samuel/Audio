import numpy as np
import librosa
import matplotlib.pyplot as plt
import librosa.display

array, sampling_rate = librosa.load(librosa.ex("trumpet"))

# D = librosa.stft(array)
# S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

S = librosa.feature.melspectrogram(y=array, sr=sampling_rate, n_mels=128, fmax=8000)
S_dB = librosa.power_to_db(S, ref=np.max)

plt.figure().set_figwidth(12)
librosa.display.specshow(S_dB, x_axis="time", y_axis="mel", sr=sampling_rate, fmax=8000)
plt.colorbar()