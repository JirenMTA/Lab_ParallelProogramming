# import sys
# import hashlib
#
# # BUF_SIZE is totally arbitrary, change for your app!
# BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
#
# md5_1 = hashlib.md5()
# sha1_1 = hashlib.sha1()
#
#
# def get_hash_code(file_path):
#     md5 = hashlib.md5()
#     with open(file_path, 'rb') as file:
#         while True:
#             data = file.read(BUF_SIZE)
#             if not data:
#                 break
#             md5.update(data)
#     hash_code = format(md5.hexdigest())
#     return hash_code
#
#
# print(get_hash_code("File1.txt"))
# print(get_hash_code("File2.txt"))

import numpy as np
import operator
import re

matrix1 = []
matrix2 = []
data = []
changer = True
data = np.genfromtxt('C:\\Users\\phamn\source\\repos\\ExampleParallelLab1\\DataMatrix.txt', delimiter=" ", dtype=int)
size = 400
t1 = []
t2 = []
for k in data:
    if changer:
        t1.append(k)
    else:
        t2.append(k)
    changer = operator.not_(changer)
    if len(t1) == size:
        matrix1.append(t1.copy())
        t1.clear()
    if len(t2) == size:
        matrix2.append(t2.copy())
        t2.clear()
test = np.matrix(matrix1, dtype=int)
test2 = np.matrix(matrix2, dtype=int)
pl1 = np.dot(test, test2)
data2 = np.genfromtxt('C:\\Users\\phamn\source\\repos\\ExampleParallelLab1\\Mul2.txt', delimiter=" ", dtype=int)
t3 = []
m = []
for k in data2:
    t3.append(k)
    if len(t3) == size:
        m.append(t3.copy())
        t3.clear()

pl2 = np.matrix(m, dtype=int)

pl1 = np.array(pl1)
pl2 = np.array(pl2)

if np.array_equal(pl1, pl2):
    print("Congratulate! You correctly multiply matrix")
else:
    print("You failed")