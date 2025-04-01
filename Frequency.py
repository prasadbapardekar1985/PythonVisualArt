"""
You are a data analyst working for a publishing company. Your task is to analyze the frequency of letters in a given string from a book excerpt. 
Create a Python script that generates a bar chart showing the frequency of each letter in the string. 
The bar chart should be visually appealing, emphasizing artistic elements such as color and style. 
Use the following string as input data: "To be, or not to be, that is the question."
"""

import collections

import matplotlib.pyplot as plt

import numpy as np

import string

data = "To be, or not to be, that is the question."

data = data.lower()

data = ''.join(filter(lambda x: x in string.ascii_lowercase, data))

counter = collections.Counter(data)

letters, counts = zip(*counter.items())

indices = np.arange(len(letters))

plt.bar(indices, counts, color='skyblue')

plt.xticks(indices, letters)

plt.xlabel('Letters')

plt.ylabel('Frequency')

plt.title('Frequency of Letters in the Given String')

plt.show()