import numpy as np

def sample_unit_simplex(shape, axis=1, sampling_function=np.random.rand,
                        dtype=np.float32):
    shape = np.asarray(shape, dtype=np.int32)
    shape[0], shape[axis] = shape[axis], shape[0]
    raw_values = sampling_function(*shape).astype(dtype)
    normalized_values = np.swapaxes(raw_values / np.sum(raw_values, axis=0),
                                    0, axis)

    return normalized_values.copy()

def is_in_unit_simplex(x, axis=1, n=None):
    is_dimension_correct = (n is None) or (x.shape[axis] == n)
    is_in_unit_cube = np.all(x >= 0.) and np.all(x <= 1.)
    is_summing_to_one = np.allclose(np.sum(x, axis=axis), 1.)

    return is_dimension_correct and is_in_unit_cube and is_summing_to_one
