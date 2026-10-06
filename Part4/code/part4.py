import numpy as np
import os

A = np.arange(1, 50).reshape(7, 7)

slices = {
    "original":    A,
    "A[::2, ::2]": A[::2, ::2],
    "A[::-1, ::-1]": A[::-1, ::-1],
}

with open("Part4/code/text/numpy_out.txt", "w") as f:
    for name, m in slices.items():
        f.write(f"# {name}\n")
        for row in m:
            f.write(",".join(map(str, row)) + "\n")
print("Wrote numpy_out.txt")