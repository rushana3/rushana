# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MrJn2lfGRyID07nMOIkehR24o94B9NZb
"""

import pandas as pd
df = pd.read_csv('/content/Customers (1).csv', sep = ';')
grouped_df = df.groupby('Profession').agg({'Income': ['mean']})
print(grouped_df)