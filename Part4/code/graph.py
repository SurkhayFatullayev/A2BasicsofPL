import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def load_matrices(path):
    """Load named matrices from a JSON file."""
    with open(path) as file:
        data = json.load(file)
    return {
        name: np.array(matrix, dtype=float)
        for name, matrix in data.items()
    }


output_directory = Path(__file__).parent / "text"
java_matrices = load_matrices(output_directory / "java_out.json")
numpy_matrices = load_matrices(output_directory / "numpy_out.json")

if java_matrices.keys() != numpy_matrices.keys():
    raise ValueError("The JSON files contain different matrix names.")

for name in numpy_matrices:
    java_matrix = java_matrices[name]
    numpy_matrix = numpy_matrices[name]
    if java_matrix.shape != numpy_matrix.shape:
        raise ValueError(f"Matrix {name} has different shapes.")
    if not np.allclose(java_matrix, numpy_matrix):
        raise ValueError(f"Matrix {name} contains different values.")

fig, axes = plt.subplots(
    len(numpy_matrices),
    2,
    figsize=(10, 4 * len(numpy_matrices)),
    squeeze=False,
)
fig.suptitle("Java and NumPy Matrix Values", fontsize=16)

for row, name in enumerate(numpy_matrices):
    java_matrix = java_matrices[name]
    numpy_matrix = numpy_matrices[name]
    minimum = min(java_matrix.min(), numpy_matrix.min())
    maximum = max(java_matrix.max(), numpy_matrix.max())

    for column, (language, matrix) in enumerate(
        (("Java", java_matrix), ("NumPy", numpy_matrix))
    ):
        axis = axes[row, column]
        image = axis.imshow(matrix, cmap="viridis", vmin=minimum, vmax=maximum)
        axis.set_title(f"{name} - {language}")
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
