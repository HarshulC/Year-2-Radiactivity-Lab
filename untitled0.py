import numpy as np
import matplotlib.pyplot as plt

# Paths to the two datasets
path1 = r"C:\Users\hc1424\Downloads\data_0.txt"
path2 = r"C:\Users\hc1424\Downloads\60keV 1cm 10000 photons_1.txt"

# Load datasets
dataset1 = np.loadtxt(path1, delimiter=",", skiprows=1)
dataset2 = np.loadtxt(path2, delimiter=",", skiprows=1)

# Extract energies (first column)
energies1 = dataset1[:, 0]
energies2 = dataset2[:, 0]

# Plot overlapping histograms
plt.figure(figsize=(8, 6))

plt.hist(
    energies1,
    bins=50,
    alpha=0.6,              # transparency
    edgecolor='black',
    label='Dataset 1'
)

plt.hist(
    energies2,
    bins=50,
    alpha=0.6,
    edgecolor='black',
    label='Dataset 2'
)

plt.xlabel("Energy Deposited in keV")
plt.ylabel("Frequency")
plt.title("Comparison of Energy Deposited in Si")
plt.legend()
plt.tight_layout()
plt.show()

