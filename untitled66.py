# -*- coding: utf-8 -*-
"""
Created on Wed May 31 18:49:45 2023

@author: LENOVO
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()