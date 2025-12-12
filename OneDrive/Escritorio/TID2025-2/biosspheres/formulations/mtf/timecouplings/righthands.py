"""
Right-hand sides for time-coupled MTF problems
This module combines the functionality of the original righthands.py
"""
from typing import Callable
import numpy as np
import biosspheres.formulations.massmatrices as mass
import biosspheres.formulations.mtf.mtf as mtf
import biosspheres.formulations.mtf.righthands as mtfrighthand


def phi_part_of_b_separable_in_space_time(
    space_b_classic_mtf: np.ndarray, time_function
) -> Callable[[float], np.ndarray]:
    """
    Create a phi function that is separable in space and time.

    Parameters
    ----------
    space_b_classic_mtf : np.ndarray
        The spatial part of the right-hand side
    time_function : Callable
        Function that takes time as input and returns a scalar

    Returns
    -------
    b_phi_part : Callable
        Function that takes time and returns the full right-hand side
    """
    def b_phi_part(time: float) -> np.ndarray:
        return space_b_classic_mtf * time_function(time)

    return b_phi_part


def phi_part_of_b_cte_space_and_time(
    big_l: int, n: int, radii: np.ndarray, cte: float
):
    """
    Create a constant phi function in space and time.

    Parameters
    ----------
    big_l : int
        Maximum degree of spherical harmonics
    n : int
        Number of spheres
    radii : np.ndarray
        Radii of the spheres
    cte : float
        Constant value

    Returns
    -------
    b_phi_part : Callable
        Function that takes time and returns the constant right-hand side
    """
    b_space = mtfrighthand.b_vector_n_spheres_mtf_cte_function(
        n, big_l, radii, cte, azimuthal=False
    )

    def time_function(time: float) -> float:
        return 1.0

    b_phi_part = phi_part_of_b_separable_in_space_time(b_space, time_function)

    return b_phi_part


def phi_part_of_b_point_source_space_and_cte_time(
    big_l: int,
    n: int,
    radii: np.ndarray,
    center_positions,
    p0,
    sigma_e,
    pii: np.ndarray,
    amplitude: float,
):
    """
    Create a point source phi function constant in time.

    Parameters
    ----------
    big_l : int
        Maximum degree of spherical harmonics
    n : int
        Number of spheres
    radii : np.ndarray
        Radii of the spheres
    center_positions : list
        Center positions of the spheres
    p0 : array-like
        Point source position
    sigma_e : float
        External conductivity
    pii : np.ndarray
        Conductivity ratios
    amplitude : float
        Amplitude of the source

    Returns
    -------
    b_phi_part : Callable
        Function that takes time and returns the point source right-hand side
    """
    x_dia, x_dia_inv = mtf.x_diagonal_with_its_inv(
        n, big_l, radii, pii, azimuthal=False
    )
    mass_n_two_j_blocks = mass.n_two_j_blocks(big_l, radii, azimuthal=False)
    b_space = amplitude * mtfrighthand.b_vector_n_spheres_mtf_point_source(
        n,
        big_l,
        center_positions,
        p0,
        radii,
        sigma_e,
        x_dia,
        mass_n_two_j_blocks,
    )

    def time_function(time: float) -> float:
        return 1.0

    b_phi_part = phi_part_of_b_separable_in_space_time(b_space, time_function)

    return b_phi_part


def phi_part_of_b_linear_space_z_cte_time(
    big_l: int,
    n: int,
    radii: np.ndarray,
    center_positions,
    cte: float,
    pii: np.ndarray,
):
    """
    Create a linear phi function in z-coordinate, constant in time.

    Parameters
    ----------
    big_l : int
        Maximum degree of spherical harmonics
    n : int
        Number of spheres
    radii : np.ndarray
        Radii of the spheres
    center_positions : list
        Center positions of the spheres
    cte : float
        Constant multiplier
    pii : np.ndarray
        Conductivity ratios

    Returns
    -------
    b_phi_part : Callable
        Function that takes time and returns the linear z right-hand side
    """
    x_dia, x_dia_inv = mtf.x_diagonal_with_its_inv(
        n, big_l, radii, pii, azimuthal=False
    )

    b_space = mtfrighthand.b_vector_n_spheres_mtf_linear_function_z(
        big_l, n, center_positions, cte, radii, x_dia
    )

    def time_function(time: float) -> float:
        return 1.0

    b_phi_part = phi_part_of_b_separable_in_space_time(b_space, time_function)

    return b_phi_part
