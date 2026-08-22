

import numpy as np

def integral(f, dx, axis=0):
    """Numerically integrate values on a uniform spatial grid."""
    return np.sum(f * dx, axis=axis) 

def energy(n):
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


def relative_error(theortical, observable): 
    """Calculates the percentage relative error between theoretical and numerical values.

    Percentage Error = |(Theoretical - Observable) / Theoretical| * 100

    Parameters:
    ----------
    theortical : float or ndarray
        The exact analytical reference value.
    observable : float or ndarray
        The computed/numerical value obtained from simulation or experiment.

    Returns:
    -------
    float or ndarray
        The relative error expressed as a percentage.
    """
    return abs((theortical - observable) / theortical) * 100