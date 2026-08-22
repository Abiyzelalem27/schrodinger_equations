

import numpy as np

def integral(f, dx, axis=0):
    """Numerically integrate values on a uniform spatial grid."""
    return np.sum(f * dx, axis=axis) 

def relative_error(theortical, observable): 
    """Calculates the percentage relative error between theoretical and numerical values.

    Percentage Error = |(Theoretical - Observable) / Theoretical| * 100

    Returns:
    -------
        The relative error expressed as a percentage.
    """
    return abs((theortical - observable) / theortical) * 100
