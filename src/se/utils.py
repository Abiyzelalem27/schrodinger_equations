

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

def hermitian(A, atol=1e-10):
    """Check A† = A."""
    return np.allclose(A.conj().T, A, atol=atol)

def unitary(A, atol=1e-10):
    """Check A†A = I."""
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return False
    I = np.eye(A.shape[0], dtype=complex)
    return np.allclose(A.conj().T @ A, I, atol=atol)

def normal(A, atol=1e-10):
    """Check [A†, A] = A†A - AA† = 0.""" 
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        return False
    commutator = A.conj().T @ A - A @ A.conj().T
    return np.allclose(commutator, 0, atol=atol)
