import numpy as np

def waveform_to_frames(waveform, frame_length, step):
    num_frames = int(np.ceil((len(waveform) - frame_length) / step)) + 1
    padding = np.zeros((frame_length + (num_frames - 1) * step - len(waveform),))
    padded_waveform = np.concatenate((waveform, padding))
    
    frames = np.zeros((frame_length, num_frames))
    for t in range(num_frames):
        start_index = t * step
        frames[:, t] = padded_waveform[start_index:start_index + frame_length]
    
    return frames

def frames_to_stft(frames):
    return np.fft.fft(frames, axis=0)

def stft_to_spectrogram(stft):
    magnitude = np.abs(stft)
    ref = np.amax(magnitude)
    spectrogram = 20 * np.log10(np.maximum(magnitude, ref / 1000.0) / ref)
    spectrogram = np.clip(spectrogram, -60, 0)
    
    return spectrogram