# regenerate_figure2_curvature_predicted.py

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

# Compute relevant decoherence derivatives
laplacian = np.zeros((L, L))
bilaplacian = np.zeros((L, L))
gradient_squared = np.zeros((L, L))
square_gamma = Gamma**2

for i in range(1, L-1):
    for j in range(1, L-1):
        laplacian[i, j] = (
            Gamma[i+1, j] + Gamma[i-1, j] + Gamma[i, j+1] + Gamma[i, j-1]
            - 4 * Gamma[i, j]
        )
        dx = (Gamma[i+1, j] - Gamma[i-1, j]) / 2
        dy = (Gamma[i, j+1] - Gamma[i, j-1]) / 2
        gradient_squared[i, j] = dx**2 + dy**2

for i in range(1, L-1):
    for j in range(1, L-1):
        bilaplacian[i, j] = (
            laplacian[i+1, j] + laplacian[i-1, j] + laplacian[i, j+1] + laplacian[i, j-1]
            - 4 * laplacian[i, j]
        )

# Expanded best-fit parameters for illustration
a1, a2, a3, a4, a5 = 0.02, 0.92, 0.03, 0.015, 0.005

# Compute predicted curvature from field equation
curvature_predicted = (
    a1 * Gamma +
    a2 * laplacian +
    a3 * bilaplacian +
    a4 * gradient_squared +
    a5 * square_gamma
)

# Plot predicted curvature field (Figure 2)
plt.figure(figsize=(6, 5))
plt.imshow(curvature_predicted, cmap='coolwarm', origin='lower')
contours = plt.contour(curvature_predicted, colors='black', linewidths=0.5)
plt.clabel(contours, inline=True, fontsize=8)
plt.title('Figure 2. Predicted Curvature from Fitted Field Equation')
plt.colorbar(label='Curvature')
plt.tight_layout()
plt.savefig('outputs/figure2_curvature_predicted.png', dpi=300)
plt.show()
