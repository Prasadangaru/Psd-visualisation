# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 20:58:23 2023

@author: prasa
"""

import pandas as pd
import matplotlib.pyplot as plt

data = {'Year': [2016, 2017, 2018, 2019, 2020],
        'Installed Capacity (GW)': [77.42, 130.25, 174.00, 204.00, 270.00],
        'Annual Installations (GW)': [34.54, 53.00, 43.75, 30.00, 62.50]}
df = pd.DataFrame(data)
df.set_index('Year', inplace=True)
ax = df.plot(kind='bar', rot=0)
ax.set_title('China Solar Industry Growth (2016-2020)')
ax.set_xlabel('Year')
ax.set_ylabel('Solar Capacity (GW)')

plt.show()