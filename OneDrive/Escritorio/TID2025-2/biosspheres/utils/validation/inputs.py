"""
Validation module - stub implementation for local use
"""
import numpy as np


def radius_validation(r, name="r"):
    """Validate radius is positive"""
    if not isinstance(r, (int, float, np.number)):
        raise TypeError(f"{name} must be a number")
    if r <= 0:
        raise ValueError(f"{name} must be positive")


def pii_validation(pi, name="pi"):
    """Validate pi parameter is positive"""
    if not isinstance(pi, (int, float, np.number)):
        raise TypeError(f"{name} must be a number")
    if pi <= 0:
        raise ValueError(f"{name} must be positive")


def numpy_array_validation(arr, name="array"):
    """Validate input is numpy array"""
    if not isinstance(arr, np.ndarray):
        raise TypeError(f"{name} must be a numpy array")


def dimensions_array_validation(arr, name="array", ndim=1):
    """Validate array has correct number of dimensions"""
    if arr.ndim != ndim:
        raise ValueError(f"{name} must have {ndim} dimensions, got {arr.ndim}")


def finite_values_in_array(arr, name="array"):
    """Validate all values in array are finite"""
    if not np.all(np.isfinite(arr)):
        raise ValueError(f"{name} contains non-finite values")


def big_l_validation(big_l, name="big_l"):
    """Validate big_l is positive integer"""
    if not isinstance(big_l, (int, np.integer)):
        raise TypeError(f"{name} must be an integer")
    if big_l < 0:
        raise ValueError(f"{name} must be non-negative")


def positive_integer_validation(n, name="n"):
    """Validate n is positive integer"""
    if not isinstance(n, (int, np.integer)):
        raise TypeError(f"{name} must be an integer")
    if n <= 0:
        raise ValueError(f"{name} must be positive")


def n_validation(n, name="n"):
    """Validate n is positive integer (alias for positive_integer_validation)"""
    positive_integer_validation(n, name)


def radii_validation(radii, name="radii"):
    """Validate radii array"""
    numpy_array_validation(radii, name)
    if radii.ndim != 1:
        raise ValueError(f"{name} must be 1-dimensional")
    if not np.all(radii > 0):
        raise ValueError(f"All values in {name} must be positive")
    finite_values_in_array(radii, name)


def positions_validation(positions, name="positions"):
    """Validate positions list/array"""
    if not isinstance(positions, (list, np.ndarray)):
        raise TypeError(f"{name} must be a list or array")


def array_of_positions_validation(positions, n, name="positions"):
    """Validate array of position vectors"""
    if len(positions) != n:
        raise ValueError(f"{name} must have length {n}")
    for i, pos in enumerate(positions):
        if not isinstance(pos, np.ndarray):
            raise TypeError(f"{name}[{i}] must be a numpy array")
        if pos.shape != (3,):
            raise ValueError(f"{name}[{i}] must have shape (3,)")


def sigma_e_validation(sigma_e, name="sigma_e"):
    """Validate external conductivity"""
    if not isinstance(sigma_e, (int, float, np.number)):
        raise TypeError(f"{name} must be a number")
    if sigma_e <= 0:
        raise ValueError(f"{name} must be positive")


def pii_validation_n_spheres(pii, n, name="pii"):
    """Validate pii array for n spheres"""
    numpy_array_validation(pii, name)
    if pii.ndim != 1:
        raise ValueError(f"{name} must be 1-dimensional")
    if len(pii) != n:
        raise ValueError(f"{name} must have length {n}")
    if not np.all(pii > 0):
        raise ValueError(f"All values in {name} must be positive")
    finite_values_in_array(pii, name)


def r_validation(r, name="r"):
    """Validate r parameter (alias for radius_validation)"""
    radius_validation(r, name)


def pi_validation(pi, name="pi"):
    """Validate pi parameter (alias for pii_validation)"""
    pii_validation(pi, name)


def bool_validation(b, name="b"):
    """Validate boolean parameter"""
    if not isinstance(b, bool):
        raise TypeError(f"{name} must be a boolean")


def two_dimensional_array_check(arr, name="array"):
    """Validate array is 2-dimensional"""
    numpy_array_validation(arr, name)
    if arr.ndim != 2:
        raise ValueError(f"{name} must be 2-dimensional")


def square_array_check(arr, name="array"):
    """Validate array is square"""
    two_dimensional_array_check(arr, name)
    if arr.shape[0] != arr.shape[1]:
        raise ValueError(f"{name} must be square, got shape {arr.shape}")


def same_shape_check(arr1, name1, arr2, name2):
    """Validate two arrays have same shape"""
    if arr1.shape != arr2.shape:
        raise ValueError(f"{name1} and {name2} must have same shape, got {arr1.shape} and {arr2.shape}")


def same_type_check(arr1, name1, arr2, name2):
    """Validate two arrays have same dtype"""
    if arr1.dtype != arr2.dtype:
        raise ValueError(f"{name1} and {name2} must have same dtype, got {arr1.dtype} and {arr2.dtype}")


def is_scipy_linear_op(op, name="op"):
    """Validate object is scipy LinearOperator"""
    # Simplified check - just verify it's not None and has basic attributes
    if op is None:
        raise ValueError(f"{name} cannot be None")
    # In full implementation would check: isinstance(op, scipy.sparse.linalg.LinearOperator)


def is_scipy_sparse_array(arr, name="array"):
    """Validate object is scipy sparse array"""
    # Simplified check
    if arr is None:
        raise ValueError(f"{name} cannot be None")
    # In full implementation would check: scipy.sparse.issparse(arr)
