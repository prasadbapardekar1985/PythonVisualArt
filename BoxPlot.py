"""
A clothing company wants to analyze the height distribution of their customers to better tailor their products.

As a data analyst, you are asked to visualize the distribution of heights of 50 randomly selected customers.

The objective is to create an aesthetically pleasing box plot using Python.

Generate the data for the heights randomly within a reasonable range and then plot the box plot.
"""

import numpy as np

import matplotlib.pyplot as plt

#Generating random height data

heights = np.random.normal(loc=170, scale=10, size=50)

#Creating the box plot

plt.figure(figsize=(10,6))

plt.boxplot(heights, patch_artist=True,

boxprops=dict(facecolor='lightblue', color='blue'),

medianprops=dict(color='red', linewidth=2),

whiskerprops=dict(color='blue'),

capprops=dict(color='blue'),

flierprops=dict(marker='o', color='red', alpha=0.5))

plt.title('Distribution of Heights')

plt.ylabel('Height (cm)')

plt.show()

