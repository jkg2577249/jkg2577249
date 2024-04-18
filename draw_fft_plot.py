import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
import argparse 
from scipy import fftpack

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=False, default='filename.wav')
args = parser.parse_args()

print("drawing plot for", args.filename)

samplerate, data = sio.wavfile.read(args.filename) 

fftsize = len(data) 
data_fft = fftpack.fft(data, fftsize)

Ts = 1/samplerate 

# Frequency axis
freqs = np.fft.fftfreq(len(data_fft)) * samplerate

# Plot FFT
plt.plot(freqs[:len(data_fft)//2], np.abs(data_fft[:len(data_fft)//2]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power')
plt.title('FFT of Audio Signal')
plt.grid(True)
plt.show()
