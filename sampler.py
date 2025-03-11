import numpy as np

def r_mat(n: int, m : int):
    return np.random.rand(n, m)
def r_square_mat(n: int):
    return np.random.rand(n, n)
def r_diag_mat(n: int):
    return np.diag(np.random.rand(n))
def r_cvec(n: int):
    return np.random.rand(n, 1)
def r_rvec(n: int):
    return np.random.rand(1, n)