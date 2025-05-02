# regenerate_figure5_energy_vs_curvature.py

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

# Compute actual curvature field (Laplacian)
curvature_actual = np.zeros((L, L))
for i in range(1, L-1):
    for j in range(1, L-1):
        curvature_actual[i, j] = (
            Gamma[i+1, j] + Gamma[i-1, j] + Gamma[i, j+1] + Gamma[i, j-1]
            - 4 * Gamma[i, j]
        )

# Flatten and filter data for scatter plot
energy_flat = energy_density.flatten()
curvature_flat = curvature_actual.flatten()

# Perform linear regression
coef = np.polyfit(energy_flat, curvature_flat, 1)
x_fit = np.linspace(energy_flat.min(), energy_flat.max(), 100)
y_fit = np.polyval(coef, x_fit)
correlation = np.corrcoef(energy_flat, curvature_flat)[0, 1]

# Plot scatter + regression line (Figure 5)
plt.figure(figsize=(8, 6))
plt.scatter(energy_flat, curvature_flat, alpha=0.6, label='Lattice sites')
plt.plot(x_fit, y_fit, color='red', label=f'Fit: y = {coef[0]:.2e}x + {coef[1]:.2e}')
plt.text(0.05, 0.95, f'Pearson r = {correlation:.2f}', transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top')
plt.xlabel('Energy Density')
plt.ylabel('Curvature')
plt.title('Figure 5. Energy Density vs Curvature')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('outputs/figure5_energy_vs_curvature.png', dpi=300)
plt.show()
