import numpy as np
import pandas as pd


def gaussian(mu, sigma, sample_size, n_samples):
    samples = []

    for K in range(n_samples):
        samples.append(np.random.normal(loc=mu, scale=sigma, size=sample_size))

    samples = pd.DataFrame(
        samples, index=["sample_" + str(i) for i in range(n_samples)]
    ).T

    mean_of_means = samples.mean().mean()
    std_of_means = samples.mean().std()

    theoretical_mean_of_means = mu
    theoretical_std_of_means = sigma / np.sqrt(sample_size)

    mean_of_sums = samples.sum().mean()
    std_of_sums = samples.sum().std()

    theoretical_mean_of_sums = sample_size * mu
    theoretical_std_of_sums = np.sqrt(sample_size) * sigma

    result = {
        "trace": np.random.normal(loc=mu, scale=sigma, size=1000).tolist(),
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

