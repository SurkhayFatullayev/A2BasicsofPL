import json

import numpy as np

A = np.arange(1, 50).reshape(7, 7)

slices = {
    "original":    A,
    "A[::2, ::2]": A[::2, ::2],
    "A[::-1, ::-1]": A[::-1, ::-1],
}

json_slices = {
    name: matrix.tolist()
    for name, matrix in slices.items()
}

with open("Part4/code/text/numpy_out.json", "w") as f:
    json.dump(json_slices, f)

print("Wrote numpy_out.json")