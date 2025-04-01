""" 
A client in the visual arts industry requires a visually appealing scatter plot for an upcoming presentation.
The scatter plot should display random points within a unit circle.
Your task is to generate this scatter plot using Python, focusing on creating a visually engaging and artistic representation.
Ensure the points are randomly distributed within the circle and utilize creative plotting techniques to enhance the visual appeal. 
"""

import numpy as np

import matplotlib.pyplot as plt

## Generate random points within a unit circle

num_points = 500

angles = np.random.uniform(0, 2 * np.pi, num_points) # Random angles

radii = np.sqrt(np.random.uniform(0, 1, num_points)) # Random radii

x_points = radii * np.cos(angles)

y_points = radii * np.sin(angles)

## Plot the points

plt.figure(figsize=(8, 8))

plt.scatter(x_points, y_points, c='blue', alpha=0.6, edgecolors='w', s=80) # Blue points with white edges and transparency

plt.title('Scatter Plot of Random Points in a Unit Circle')

plt.xlim(-1, 1)

plt.ylim(-1, 1)

plt.gca().set_aspect('equal', adjustable='box') # Ensure the aspect ratio is equal to keep the circle shape

plt.grid(True, which='both', linestyle='--', linewidth=0.5) # Adding grid for better visual reference

plt.show()
