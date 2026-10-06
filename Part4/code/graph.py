from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def load_matrices(path):
    """Load matrix values and ignore section names."""
    matrices = []
    current_matrix = []

    with open(path) as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            is_header = line.startswith("#") or line.startswith("Original")
            if is_header:
                if current_matrix:
                    matrices.append(np.array(current_matrix))
                    current_matrix = []
                continue

            current_matrix.append(
                [float(value) for value in line.replace(",", " ").split()]
            )

    if current_matrix:
        matrices.append(np.array(current_matrix))

    return matrices


output_directory = Path(__file__).parent / "text"
java_matrices = load_matrices(output_directory / "java_out.txt")
numpy_matrices = load_matrices(output_directory / "numpy_out.txt")

if len(java_matrices) != len(numpy_matrices):
    raise ValueError("The files contain a different number of matrices.")

for index, (java_matrix, numpy_matrix) in enumerate(
    zip(java_matrices, numpy_matrices),
    start=1,
):
    if java_matrix.shape != numpy_matrix.shape:
        raise ValueError(f"Matrix {index} has different shapes.")
    if not np.allclose(java_matrix, numpy_matrix):
        raise ValueError(f"Matrix {index} contains different values.")

fig, axes = plt.subplots(
    len(numpy_matrices),
    2,
    figsize=(10, 4 * len(numpy_matrices)),
    squeeze=False,
)
fig.suptitle("Java and NumPy Matrix Values", fontsize=16)

for row, (java_matrix, numpy_matrix) in enumerate(
    zip(java_matrices, numpy_matrices)
):
    minimum = min(java_matrix.min(), numpy_matrix.min())
    maximum = max(java_matrix.max(), numpy_matrix.max())

    for column, (language, matrix) in enumerate(
        (("Java", java_matrix), ("NumPy", numpy_matrix))
    ):
        axis = axes[row, column]
        image = axis.imshow(matrix, cmap="viridis", vmin=minimum, vmax=maximum)
        axis.set_title(f"Matrix {row + 1} - {language}")
        axis.set_xlabel("Column")
        axis.set_ylabel("Row")
        axis.set_xticks(range(matrix.shape[1]))
        axis.set_yticks(range(matrix.shape[0]))

        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                axis.text(j, i, f"{matrix[i, j]:g}", ha="center", va="center")

        fig.colorbar(image, ax=axis)

plt.tight_layout()
plt.show()
