'''

Author: Jordan Cahill
Date: 02/11/2018

Script to perform a discrete cosine transform on a 2D square matrix.
Takes the length M of the input matrix and calculates T, the DCT matrix for an M x M matrix.
The input matrix M and DCT matrix T are multiplied, and the product is then multiplied by T-transpose
to get the DCT of M.

'''

import math
import numpy as np

# If the program is run as main, calculates DCT of this sample matrix
sample = [[100, 100, 100, 100, 100, 100, 100, 100],
          [100, 100, 100, 100, 100, 100, 100, 100],
          [100, 100, 100, 100, 100, 100, 100, 100],
          [100, 100, 100, 100, 100, 100, 100, 100],
          [100, 100, 100, 100, 100, 100, 100, 100],
          [100, 100, 100, 100, 100, 100, 100, 100],
          [100, 100, 100, 100, 100, 100, 100, 100],
          [100, 100, 100, 100, 100, 100, 100, 100]]

# Calculate the DCT Matrix for an M x M matrix
def get_dct_matrix(m):

    dct_matrix = np.empty((m, m))

    for p in range(m):
        for q in range(m):
            if p == 0: # Case: First row
                dct_matrix[p, q] = 1/math.sqrt(m)
            else: # Every other row
                dct_matrix[p, q] = (math.sqrt(2/m))*math.cos((math.pi*((2*q)+1)*p)/(2*m))
    return dct_matrix


def dct(a):
    t = get_dct_matrix(len(a))
    b = np.matmul(t, a)
    out = np.matmul(b, t.T)
    return out


if __name__ == '__main__':
    print("Running DCT on 8x8 sample array of values '100'...")
    print("Output array: ")
    print(dct(sample))
