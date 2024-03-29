# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12gnUOTJL2cQmcE1PpV2xoPa5ls8YsezV
"""

import numpy as np

arr = np.random.randint(1, 11, size=100)
print(arr)
per7 = np.mean(arr > 7) * 100
print(per7)

experiments = 1000
rez = [np.mean(np.random.randint(1, 11, size=100) > 7) * 100 for _ in range(experiments)]
per20 = np.mean(np.array(rez) == 20)
print(per20)

mtc = np.tile(np.arange(1, 11), (10, 1))
print(mtc)

column_sums = np.sum(mtc, axis=0)
arr, per7, per20, mtc, column_sums