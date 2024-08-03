import numpy as np
import matplotlib.pyplot as plt

def compute_fft(f1, f2, fs, duration):
    # Generate time vector
    t = np.arange(0, duration, 1/fs)
    
    # Generate the signal
    s_t = np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)
    
    # Compute FFT
    fft_result = np.fft.fft(s_t)
    
    # Frequency vector
    freqs = np.fft.fftfreq(len(fft_result), 1/fs)
    
    # Only take the positive frequencies
    positive_freqs = freqs[:len(freqs)//2]
    positive_fft = np.abs(fft_result)[:len(fft_result)//2]
    
    # Plotting the signal
    plt.figure(figsize=(12, 6))
    
    # Time domain plot
    plt.subplot(2, 1, 1)
    plt.plot(t, s_t)
    plt.title('Time Domain Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
    # Frequency domain plot
    plt.subplot(2, 1, 2)
    plt.plot(positive_freqs, positive_fft)
    plt.title('Frequency Domain (FFT)')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    
    plt.tight_layout()
    plt.show()

# Parameters
f1 = 50   # Frequency 1 in Hz
f2 = 120  # Frequency 2 in Hz
fs = 1000 # Sampling frequency in Hz
duration = 1 # Duration in seconds

# Call the function
compute_fft(f1, f2, fs, duration)
