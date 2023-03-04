# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 20:54:29 2023

@author: prasa
"""

import pandas as pd
import matplotlib.pyplot as plt

countries = ['China', 'United States', 'Japan', 'Germany', 'India']
values_2016 = [77.42, 40.28, 42.66, 41.32, 9.00]
values_2020 = [253.00, 97.67, 62.61, 52.44, 44.81]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))

ax1.pie(values_2016, labels=countries, autopct='%1.1f%%')
ax1.set_title('Solar Energy Consumption in 2016')

ax2.pie(values_2020, labels=countries, autopct='%1.1f%%')
ax2.set_title('Solar Energy Consumption in 2020')

plt.show()
