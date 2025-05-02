# regenerate_figure4_energy_density.py

import numpy as np
import matplotlib.pyplot as plt

import os, pathlib
pathlib.Path("outputs").mkdir(exist_ok=True)

# Parameters
L = 16
source_positions = [(5, 5), (10, 10)]
np.random.seed(42)

# Create decoherence field
Gamma = np.zeros((L, L))
for (cx, cy) in source_positions:
    for i in range(L):
        for j in range(L):
            r2 = (i - cx)**2 + (j - cy)**2
            Gamma[i, j] += np.exp(-r2 / 10.0) * 0.05
Gamma += np.random.normal(loc=0, scale=0.001, size=(L, L))

# Compute gradient magnitude squared
gradient_squared = np.zeros((L, L))
for i in range(1, L-1):
    for j in range(1, L-1):
        dx = (Gamma[i+1, j] - Gamma[i-1, j]) / 2
        dy = (Gamma[i, j+1] - Gamma[i, j-1]) / 2
        gradient_squared[i, j] = dx**2 + dy**2

# Compute energy density
energy_density = Gamma**2 + gradient_squared

# Plot energy density field (Figure 4)
plt.figure(figsize=(6, 5))
plt.imshow(energy_density, cmap='plasma', origin='lower')
contours = plt.contour(energy_density, colors='black', linewidths=0.5)
plt.clabel(contours, inline=True, fontsize=8)
plt.title('Figure 4. Emergent Energy Density Field')
plt.colorbar(label='Energy Density')
plt.tight_layout()
plt.savefig('outputs/figure4_energy_density.png', dpi=300)
plt.show()
