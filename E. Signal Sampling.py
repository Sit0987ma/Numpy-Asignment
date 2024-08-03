import numpy as np
import matplotlib.pyplot as plt

# Parameters
f1 = 50  # Hz
f2 = 120  # Hz
fs = 1000  # Sampling frequency in Hz
T = 1  # Duration in seconds
N = T * fs  # Number of samples

# Time vector
t = np.linspace(0, T, N, endpoint=False)

# Signal
s = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)

# FFT
S = np.fft.fft(s)
S_magnitude = np.abs(S) / N
frequencies = np.fft.fftfreq(N, 1/fs)

# Only take the positive half of the spectrum
positive_frequencies = frequencies[:N // 2]
positive_magnitude = S_magnitude[:N // 2]

# Plotting the frequency spectrum
plt.figure(figsize=(10, 6))
plt.plot(positive_frequencies, positive_magnitude)
plt.title('Frequency Spectrum of the Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()
