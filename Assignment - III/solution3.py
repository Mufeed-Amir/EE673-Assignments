import numpy as np

# 1. Define the Transition Matrix P
# States order: [11, 12, 21, 22]
P = np.array([
    [0.50, 0.25, 0.25, 0.00],  # From state 11
    [0.25, 0.25, 0.25, 0.25],  # From state 12
    [0.25, 0.25, 0.25, 0.25],  # From state 21
    [0.00, 0.25, 0.25, 0.50]   # From state 22
])

# 2. Compute the Stationary Distribution (pi = pi * P)
# We solve the eigenvalue problem for the transpose of P: P^T * pi^T = 1 * pi^T
eigenvalues, eigenvectors = np.linalg.eig(P.T)

# Find the eigenvector corresponding to the eigenvalue 1
index = np.isclose(eigenvalues, 1)
pi_unnormalized = eigenvectors[:, index].real.flatten()

# Normalize so probabilities sum to 1
pi = pi_unnormalized / pi_unnormalized.sum()
print(f"Stationary Distribution [11, 12, 21, 22]: {pi}")

# 3. Compute Average Throughput
# In states 11 and 22, throughput = 1 packet. In states 12 and 21, throughput = 2 packets.
throughput_per_state = np.array([1, 2, 2, 1])
avg_throughput = np.sum(pi * throughput_per_state)

print(f"Average Throughput: {avg_throughput} packets per slot")
print(f"Normalized average throughput (relative to max 2 packets): {avg_throughput / 2:.2f}")