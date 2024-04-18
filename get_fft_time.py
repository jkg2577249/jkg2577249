import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
import argparse 
from scipy import fftpack
import time

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=False, default='filename.wav')
args = parser.parse_args()

print("drawing plot for", args.filename)

samplerate, data = sio.wavfile.read(args.filename)

# Start measuring time
start_time = time.time()

fftsize = len(data)
data_fft = fftpack.fft(data, fftsize)

# End measuring time
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("FFT execution time:", elapsed_time, "seconds")
