#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""

import pandas as pd
import numpy as np



df = pd.read_csv("lianjia.csv")
print(df)
print(df.info())
print(df.describe())
print(len(df))

df.drop_duplicates(subset=['house_code'], keep='first', inplace=True)
print(len(df))
#
df.to_csv("beijing_4-14.csv")




if __name__ == '__main__':
    pass

