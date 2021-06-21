import numpy as np
import os
import time
import math

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
matrix1_path = os.path.join(THIS_FOLDER, '1.txt')
matrix2_path = os.path.join(THIS_FOLDER, '2.txt')
matrix3_path = os.path.join(THIS_FOLDER, '3.txt')
matrix4_path = os.path.join(THIS_FOLDER, '4.txt')
matrix5_path = os.path.join(THIS_FOLDER, '5.txt')
matrix6_path = os.path.join(THIS_FOLDER, '6.txt')
matrix7_path = os.path.join(THIS_FOLDER, '7.txt')
matrix8_path = os.path.join(THIS_FOLDER, '8.txt')
matrix9_path = os.path.join(THIS_FOLDER, '9.txt')
matrix10_path = os.path.join(THIS_FOLDER, '10.txt')


#matrix1 = np.loadtxt(matrix1_path, dtype=int)
#matrix2 = np.loadtxt(matrix2_path, dtype=int)
#matrix3 = np.loadtxt(matrix3_path, dtype=int)
#matrix4 = np.loadtxt(matrix4_path, dtype=int)
#matrix5 = np.loadtxt(matrix5_path, dtype=int)
#matrix6 = np.loadtxt(matrix6_path, dtype=int)
#matrix7 = np.loadtxt(matrix7_path, dtype=int)
#matrix8 = np.loadtxt(matrix8_path, dtype=int)
#matrix9 = np.loadtxt(matrix9_path, dtype=int)
#matrix10 = np.loadtxt(matrix10_path, dtype=int)
#print('matrices are loaded')


def find_next_a(mat, a, min_loss):
    overlap = mat[(mat[:, 1] >= a) & (mat[:, 0] < a)]
    while overlap.size != 0:
        # print(overlap)
        loss = a - max(overlap[:, 0])
        if min_loss > loss:
            min_loss = loss
        a = min(overlap[:, 0])
        overlap = mat[(mat[:, 1] >= a) & (mat[:, 0] < a)]
    # return a


def find_next_b(mat, a):
    mat = mat[(mat[:, 1] < a)]
    return max(mat[:, 1])


# check case of complete overlap


def fire_lifeguard(mat):
    min_loss = math.inf
    covered_time = 0
    b = max(mat[:, 1])
    a = mat[np.argmax(mat[:, 1]), 0]
    # print(mat)
    while mat.size != 0:
        find_next_a(mat, a, min_loss)
        covered_time += (b - a)
        mat = mat[(mat[:, 1] < a)]
        if mat.size != 0:
            b = max(mat[:, 1])
            a = mat[np.argmax(mat[:, 1]), 0]
            # print(mat)

    print(covered_time)
    print(min_loss)

matrix = np.loadtxt(matrix2_path, dtype=int)
print(np.sort(matrix, axis=0))
t0 = time.time()
fire_lifeguard(matrix)
t1 = time.time()
print('runtime: ', (t1 - t0))

