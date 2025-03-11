import numpy as np

def r_mat(n: int, m : int):
    return np.random.rand(n, m)
def r_mat_range(n_lo, n_hi, m_lo, m_hi):
    n = np.random.randint(n_lo, n_hi)
    m = np.random.randint(m_lo, m_hi)
    return r_mat(n, m), (n, m)
def r_square_mat(n: int):
    return np.random.rand(n, n)
def r_diag_mat(n: int):
    return np.diag(np.random.rand(n))
def r_cvec(n: int):
    return np.random.rand(n, 1)
def r_rvec(n: int):
    return np.random.rand(1, n)