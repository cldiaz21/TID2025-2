from typing import Callable
import numpy as np

# Este módulo requiere que se importen previamente:
# - biosspheres.formulations.massmatrices as mass
# - biosspheres.formulations.mtf.mtf as mtf
# - biosspheres.formulations.mtf.righthands as mtfrighthand
# Estos se importarán en el notebook antes de usar este módulo


def phi_part_of_b_separable_in_space_time(
    space_b_classic_mtf: np.ndarray, time_function
) -> Callable[[float], np.ndarray]:

    def b_phi_part(time: float) -> np.ndarray:
        return space_b_classic_mtf * time_function(time)

    return b_phi_part


def phi_part_of_b_cte_space_and_time(
    big_l: int, n: int, radii: np.ndarray, cte: float, mtfrighthand=None
):
    if mtfrighthand is None:
        raise ImportError("Se requiere el módulo mtfrighthand. Importalo como: import biosspheres.formulations.mtf.righthands as mtfrighthand")

    b_space = mtfrighthand.b_vector_n_spheres_mtf_cte_function(
        n, big_l, radii, cte, azimuthal=False
    )

    def time_function(time: float) -> np.ndarray:
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
    mtf=None,
    mass=None,
    mtfrighthand=None
):
    if mtf is None or mass is None or mtfrighthand is None:
        raise ImportError("Se requieren los módulos mtf, mass y mtfrighthand")

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

    def time_function(time: float) -> np.ndarray:
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
    mtf=None,
    mtfrighthand=None
):
    if mtf is None or mtfrighthand is None:
        raise ImportError("Se requieren los módulos mtf y mtfrighthand")

    x_dia, x_dia_inv = mtf.x_diagonal_with_its_inv(
        n, big_l, radii, pii, azimuthal=False
    )

    b_space = mtfrighthand.b_vector_n_spheres_mtf_linear_function_z(
        big_l, n, center_positions, cte, radii, x_dia
    )

    def time_function(time: float) -> np.ndarray:
        return 1.0

    b_phi_part = phi_part_of_b_separable_in_space_time(b_space, time_function)

    return b_phi_part
