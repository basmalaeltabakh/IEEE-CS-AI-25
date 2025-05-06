import numpy as np

n, m = map(int, input().split())

pixels = []
for _ in range(n):
    row = input().split()
    pixels.append(row)

arr = np.array(pixels)

colored_pixels = {'C', 'M', 'Y'}

# Check if any pixel in the matrix is one of the colored pixels
if np.isin(arr, list(colored_pixels)).any():
    print("#Color")
else:
    print("#Black&White")
