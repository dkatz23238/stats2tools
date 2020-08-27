from stat2tools.exponential import exponential
from stat2tools.gamma import gamma
from stat2tools.normal import gaussian


def test_result(r):
    d1 = abs(r["mean_of_means"] - r["theoretical_mean_of_means"])
    d2 = abs(r["std_of_means"] - r["theoretical_std_of_means"])
    d3 = abs(r["mean_of_sums"] - r["theoretical_mean_of_sums"])
    d4 = abs(r["std_of_sums"] - r["theoretical_std_of_sums"])

    assert d1 < 1
    assert d2 < 1
    assert d3 < 10
    assert d4 < 10


l = 0.1
sample_size = 55
n_samples = 100
r = exponential(l, sample_size, n_samples)
test_result(r)

alpha = 3
theta = 2
sample_size = 55
n_samples = 100
r = gamma(alpha, theta, sample_size, n_samples)
test_result(r)


mu = 10
sigma = 4
sample_size = 55
n_samples = 100
r = gaussian(mu, sigma, sample_size, n_samples)
test_result(r)
