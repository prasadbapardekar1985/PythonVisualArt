import numpy as np

import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)

y = np.sin(x)

plt.figure(figsize=(10, 6))

plt.plot(x, y, color='darkcyan', linestyle='--', linewidth=2, label='Sine Wave')

plt.title('Artistic Sine Wave Plot', fontsize=20, fontweight='bold')

plt.xlabel('X-axis (radians)', fontsize=14)

plt.ylabel('Y-axis', fontsize=14)

plt.axhline(0, color='grey', linewidth=0.8)

plt.axvline(np.pi, color='grey', linewidth=0.8, linestyle=':')

plt.legend(loc='upper right')

plt.grid(True, which='both', linestyle=':', linewidth=0.5)

plt.annotate('Peak', xy=(np.pi / 2, 1), xytext=(np.pi / 2, 1.5),

arrowprops=dict(facecolor='black', shrink=0.05),

fontsize=12, fontweight='bold', color='purple')

plt.show()

