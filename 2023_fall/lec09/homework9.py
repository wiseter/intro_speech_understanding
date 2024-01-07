import numpy as np

def fourier_synthesis(num_harmonics, X, T0):
    N = len(X)
    x = np.zeros(N)  # Initialize the output array

    for n in range(N):
        sum_harmonics = 0
        for l in range(1, num_harmonics + 1):
            index = l * N // T0
            if index < N:  # Ensure the index does not exceed the length of X
                magnitude = np.abs(X[index])
                phase = np.angle(X[index])
                sum_harmonics += magnitude * np.cos(2 * np.pi * l * n / T0 + phase)
        x[n] = (2 / N) * sum_harmonics

    return x


