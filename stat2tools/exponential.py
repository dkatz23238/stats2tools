import numpy as np
import pandas as pd

generators = {"exponential": np.random.exponential, "normal": np.random.normal}


def exponential(l, sample_size, n_samples):
    samples = []

    for K in range(n_samples):
        samples.append(np.random.exponential(scale=1 / l, size=sample_size))

    samples = pd.DataFrame(
        samples, index=["sample_" + str(i) for i in range(n_samples)]
    ).T

    mu = 1 / l
    sigma = (1 / l) / np.sqrt(sample_size)

    mean_of_means = samples.mean().mean()
    std_of_means = samples.mean().std()

    theoretical_mean_of_means = 1 / l
    theoretical_std_of_means = 1 / l / np.sqrt(sample_size)

    mean_of_sums = samples.sum().mean()
    std_of_sums = samples.sum().std()

    theoretical_mean_of_sums = sample_size * 1 / l
    theoretical_std_of_sums = np.sqrt(sample_size) * 1 / l

    result = {
        "trace": np.random.exponential(scale=1 / l, size=2000).tolist(),
        "mean_of_means": mean_of_means,
        "std_of_means": std_of_means,
        "theoretical_mean_of_means": theoretical_mean_of_means,
        "theoretical_std_of_means": theoretical_std_of_means,
        "mean_of_sums": mean_of_sums,
        "std_of_sums": std_of_sums,
        "theoretical_mean_of_sums": theoretical_mean_of_sums,
        "theoretical_std_of_sums": theoretical_std_of_sums,
        "simulation_means": samples.mean().tolist(),
        "simulation_sums": samples.sum().tolist(),
        "theoretical_sample_of_means": np.random.normal(
            theoretical_mean_of_means, theoretical_std_of_means, size=n_samples
        ).tolist(),
        "theoretical_sample_of_sums": np.random.normal(
            theoretical_mean_of_sums, theoretical_std_of_sums, size=n_samples
        ).tolist(),
    }
    return result
