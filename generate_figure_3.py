import numpy as np
from scipy.stats import kendalltau
import matplotlib.pyplot as plt

def bootstrap_kendall_tau(reference, prediction, n=1000, confidence_level=0.90):
    tau_values = []
    n_samples = len(reference)
    for _ in range(n):
        indices = np.random.randint(0, n_samples, n_samples)
        sample_ref = np.array(reference)[indices]
        sample_pred = np.array(prediction)[indices]
        tau, _ = kendalltau(sample_ref, sample_pred)
        tau_values.append(tau)

    tau_values_sorted = np.sort(tau_values)
    cdf = np.arange(1, len(tau_values_sorted) + 1) / len(tau_values_sorted)

    return tau_values_sorted, cdf

if __name__ == "__main__":

    #Vectors:
    Eclipse = [1, 2, 3, 4, 2, 1, 3, 4, 2, 3, 4, 1, 4, 1, 3, 2, 3, 2, 1, 4, 4, 1, 3, 2, 1, 3, 2, 4, 2, 3, 1, 4, 1, 3, 2, 4, 4, 1, 3, 2, 3, 1, 4, 2, 1, 3, 2, 4, 3, 4, 2, 1]
    DL= [1, 2, 3, 4, 1, 2, 3, 4, 1, 4, 2, 3, 3, 2, 1, 4, 3, 4, 2, 1, 4, 3, 1, 2, 1, 3, 2, 4, 4, 3, 2, 1, 1, 2, 3, 4, 1, 4, 2, 3, 4, 1, 3, 2, 4, 3, 1, 2, 1, 3, 2, 4]
    R01=[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 1, 2, 3, 3, 4, 2, 1, 3, 4, 2, 1, 1, 4, 2, 3, 2, 3, 4, 1, 2, 1, 3, 4, 2, 3, 4, 1, 4, 3, 2, 1, 4, 3, 1, 2, 1, 2, 3, 4]
    R02=[2, 4, 3, 1, 1, 2, 4, 3, 1, 2, 3, 4, 3, 1, 2, 4, 4, 3, 2, 1, 1, 2, 3, 4, 1, 4, 2, 3, 4, 3, 2, 1, 1, 2, 3, 4, 2, 3, 1, 4, 2, 1, 4, 3, 3, 4, 1, 2, 1, 2, 4, 3]
    R03=[2, 4, 3, 1, 1, 3, 2, 4, 1, 2, 4, 3, 4, 1, 2, 3, 4, 3, 2, 1, 4, 2, 3, 1, 1, 4, 2, 3, 4, 3, 2, 1, 2, 1, 3, 4, 1, 2, 3, 4, 2, 1, 4, 3, 3, 4, 1, 2, 1, 2, 3, 4]
    R04=[1, 2, 4, 3, 1, 4, 3, 2, 1, 4, 3, 1, 4, 2, 1, 3, 4, 3, 2, 1, 1, 3, 2, 1, 2, 4, 1, 3, 4, 3, 2, 1, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 1, 3, 4, 2, 1, 1, 2, 3, 4]

    # Plotting
    plt.figure(figsize=(12, 8))

    kendalls_tau_sorted, cdf = bootstrap_kendall_tau(Eclipse, DL)
    kendalls_tau_sorted_r01, cdf_r01 = bootstrap_kendall_tau(Eclipse, R01)
    kendalls_tau_sorted_r02, cdf_r02 = bootstrap_kendall_tau(Eclipse, R02)
    kendalls_tau_sorted_r03, cdf_r03 = bootstrap_kendall_tau(Eclipse, R03)
    kendalls_tau_sorted_r04, cdf_r04 = bootstrap_kendall_tau(Eclipse, R04)

    # Plot the CDF for all comparisons in one plot with assigned colors
    plt.plot(kendalls_tau_sorted, cdf, marker='.', linestyle='none', color='orange', label='Eclipse vs DL')
    plt.plot(kendalls_tau_sorted_r01, cdf_r01, marker='.', linestyle='none', color='blue', label='Eclipse vs R01')
    plt.plot(kendalls_tau_sorted_r02, cdf_r02, marker='.', linestyle='none', color='purple', label='Eclipse vs R02')
    plt.plot(kendalls_tau_sorted_r03, cdf_r03, marker='.', linestyle='none', color='red', label='Eclipse vs R03')
    plt.plot(kendalls_tau_sorted_r04, cdf_r04, marker='.', linestyle='none', color='pink', label='Eclipse vs R04')
    plt.title('Cumulative Distribution of Kendall\'s Tau Values\n(Eclipse vs Predictions from Bootstrapping)')
    plt.xlabel('Kendall\'s Tau Value')
    plt.ylabel('CDF')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()