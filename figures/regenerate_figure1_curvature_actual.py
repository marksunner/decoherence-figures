# regenerate_figure1_curvature_actual.py

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

# Compute Laplacian (actual curvature)
curvature_actual = np.zeros((L, L))
for i in range(1, L-1):
    for j in range(1, L-1):
        curvature_actual[i, j] = (
            Gamma[i+1, j] + Gamma[i-1, j] + Gamma[i, j+1] + Gamma[i, j-1]
            - 4 * Gamma[i, j]
        )

# Plot the curvature field (Figure 1)
plt.figure(figsize=(6, 5))
plt.imshow(curvature_actual, cmap='coolwarm', origin='lower')
contours = plt.contour(curvature_actual, colors='black', linewidths=0.5)
plt.clabel(contours, inline=True, fontsize=8)
plt.title('Figure 1. Simulated Emergent Curvature Field')
plt.colorbar(label='Curvature')
plt.tight_layout()
plt.savefig('outputs/figure1_curvature_actual.png', dpi=300)
plt.show()
