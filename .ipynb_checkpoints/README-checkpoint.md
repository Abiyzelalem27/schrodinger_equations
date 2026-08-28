

# Schrödinger Equation

A modular Python package designed to numerically solve the Time-Independent Schrödinger Equation (TISE) for a particle trapped in an Infinite Square Well using finite difference matrix operators. Benchmark results are validated against exact analytical solutions.

---
s
## Key Features

* **Modular Package Architecture:** Standard `src/` layout configured with `pyproject.toml` for editable local installations (`pip install -e .`).
* **Finite Difference Solver:** Constructs sparse/dense discrete Hamiltonian matrices and extracts energy eigenvalues using `numpy.linalg.eigh`.
* **Analytical Validation:** Compares numerical wavefunctions $\psi(x)$ and energy levels $E_n$ against theoretical quantum state solutions.
* **Visualization Tools:** Plotting utilities for evaluating probability densities $\vert{}\psi_n(x)\vert{}^2$ and node structures.

---

## Installation

Clone the repository and install the package in editable mode:

```bash
git clone [https://github.com/Abiyzelalem27/schrodinger_equations.git]
cd schrodinger-equations
pip install -e .