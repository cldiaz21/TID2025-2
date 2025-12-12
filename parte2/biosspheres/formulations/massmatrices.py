"""
Mass matrices for formulations
"""
import numpy as np


def n_two_j_blocks(big_l, radii, azimuthal=False):
    """
    Construct mass matrix blocks.

    Parameters
    ----------
    big_l : int
        Maximum degree of spherical harmonics
    radii : np.ndarray
        Radii of spheres
    azimuthal : bool
        Whether to use azimuthal symmetry

    Returns
    -------
    mass_matrix : np.ndarray
        Mass matrix blocks
    """
    if azimuthal:
        num = big_l + 1
    else:
        num = (big_l + 1) ** 2

    n = len(radii)
    mass_matrix = np.zeros((2 * n * num, num))

    # Simplified implementation - you may need actual mass matrix computation
    for i in range(n):
        mass_matrix[2*i*num:(2*i+1)*num, :] = np.eye(num) * radii[i]**2
        mass_matrix[(2*i+1)*num:(2*i+2)*num, :] = np.eye(num) * radii[i]**2

    return mass_matrix
