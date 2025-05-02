# Decoherence Geometry – Figure Reproducibility Archive

This repository contains the exact Python 3 scripts used to regenerate **Figures 1-5** in  

> *Decoherence Geometry: Gravitational Curvature as an Emergent Record of Quantum Information Fragmentation* (rev 0.5.4).

Each script synthesises a 2-D spin-lattice decoherence field, derives the required observables, and exports a 300 dpi PNG identical to the corresponding panel in the manuscript.  
The simulations are fully self-contained and deterministic (`np.random.seed(42)`).

---

## Directory structure

```text
.
├── requirements.txt
└── figures/
    ├── regenerate_figure1_curvature_actual.py
    ├── regenerate_figure2_curvature_predicted.py
    ├── regenerate_figure3_curvature_error.py
    ├── regenerate_figure4_energy_density.py
    ├── regenerate_figure5_energy_vs_curvature.py
    └── outputs/            # created automatically on first run
        ├── figure1_curvature_actual.png
        ├── figure2_curvature_predicted.png
        ├── figure3_curvature_error.png
        ├── figure4_energy_density.png
        └── figure5_energy_vs_curvature.png


# 1 · create & activate a clean env
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 2 · install the minimal dependencies
pip install -r requirements.txt   # numpy, matplotlib

# 3 · build every panel in one go
cd figures
for f in regenerate_figure*.py; do python "$f"; done
# PNGs will appear in figures/outputs/


