import numpy as np


def qr_algorithm(A, num_iterations: int = 1000):
    A_k = A.copy()

    for _ in range(num_iterations):
        Q, R = np.linalg.qr(A_k)  # QR decomposition
        A_k = R @ Q  # Update A_k for the next iteration

    eigenvalues = np.diag(A_k)  # Extract eigenvalues from the diagonal
    return eigenvalues, Q  # Return eigenvalues and the orthogonal matrix Q


# Example matrix
A = np.array([[4, 1, 1], [1, 3, -1], [1, -1, 2]])

# Example usage
eigenvalues_qr, eigenvector_qr = qr_algorithm(A)
print("\nQR Algorithm:")
print("Eigenvalues:", eigenvalues_qr)
print("Eigenvectors:\n", eigenvector_qr)
