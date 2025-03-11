import numpy as np
import matplotlib.pyplot as plt

def display(n_lo, n_hi, compute, sampler = "Integer", expected = None, samples=500, 
        scientific=False, axx_name="n", axy_name="", **kwargs):
    """
    n_lo : int
        lower bound for n
    n_hi : int
        upper bound for n
    compute : function
        Performs and times a computation, given input of "ns",
        returns (ns, times, res)
    sampler : string
        "Integer" takes random integer from (n_lo, n_hi)
        "Poisson" takes random from Poisson(lambda=n_hi) shifted right n_lo, rounded 
        "Exp" takes random from Exp(lambda=n_hi) shifted right n_lo, rounded
    """
    
    # Sampling performance
    ns = None
    if sampler == "Integer":
        ns = np.random.randint(n_lo, n_hi, size=samples)
    elif sampler == "Poisson":
        ns = np.round(np.random.poisson(n_hi, size=samples) + n_lo).astype(int)
    elif sampler == "Exp":
        ns = np.round(np.random.exponential(n_hi, size=samples) + n_lo).astype(int)
    ns, time, _ = compute(ns)
    scaled_n = np.log(ns)
    scaled_time = np.log(time)

    plt.scatter(scaled_n, scaled_time, s=1)
    # Removing crazy outliers to look better
    t_lo = np.percentile(scaled_time, 1)
    t_hi = np.percentile(scaled_time, 99)
    padding = 0.2 * (t_hi - t_lo)
    t_max = t_hi + padding
    t_min = t_lo - padding
    # Line of best fit
    m, b = np.polyfit(scaled_n, scaled_time, 1)
    plt.plot(scaled_n, m * scaled_n + b, 
                color='red', label=f'time={m:.2f}{axx_name} + {b:.2f}', **kwargs)
    ax = plt.gca()
    if (not scientific):
        ax.ticklabel_format(useOffset=False, style='plain')
    plt.xlabel(axx_name)
    plt.ylabel(axy_name)
    plt.ylim((t_min, t_max))
    plt.legend()
    plt.show()