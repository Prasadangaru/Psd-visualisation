# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 21:02:54 2023

@author: prasa
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Country': ['China', 'United States', 'Japan', 'Germany', 'India'],
    '2016': [77.42, 40.28, 42.66, 41.32, 9.00],
    '2017': [130.25, 47.10, 47.64, 42.54, 12.92],
    '2018': [177.00, 64.20, 50.63, 45.43, 28.16],
    '2019': [223.00, 76.00, 55.50, 49.30, 40.00],
    '2020': [253.00, 97.67, 62.61, 52.44, 44.81]
}

df = pd.DataFrame(data)
df.set_index('Country', inplace=True)

df.plot(kind='line')
plt.title('Solar Energy Consumption of Five Countries from 2016 to 2020')
plt.xlabel('Year')
plt.ylabel('Solar Energy Consumption (in GW)')

plt.show()