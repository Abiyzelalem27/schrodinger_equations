

import numpy as np

def true_psi(n, x, a):
    r"""
    Analytical spatial wavefunction \psi_n(x) for an 1D Infinite Square Well.

    \psi_n(x) = \sqrt{\frac{2}{a}} \sin\left(\frac{n \pi x}{a}\right)

    Parameters:
    ----------
    n : int
        Quantum number / energy state (n = 1, 2, 3, ...)
    x : float or ndarray
        Position vector inside the well (0 <= x <= a)

    Returns:
    -------
    ndarray or float
        The exact analytical wavefunction value(s) at position x.
    """
    return np.sqrt(2 / a) * np.sin(n * np.pi * x / a) 
    
def energy(n, hbar, m, a):
    """Calculates the analytical energy eigenvalue En for an 1D Infinite Square Well.

    E_n = (hbar^2 * pi^2 * n^2) / (2 * m * a^2)

    Parameters:
    ----------
    n : int
        Quantum number / energy state (n = 1, 2, 3, ...)

    Returns:
    -------
    float
        The theoretical energy of the nth state in Joules (or units matching
        hbar, m, a).
    """
    return hbar**2 * np.pi**2 * n**2 / (2 * m * a**2)