import numpy as np
import time

for size in [100, 200, 500]:
    print(f"--------------------------------------------------")
    print(f"Testing matrix size: {size}x{size}")
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    start = time.perf_counter()
    C = np.matmul(A, B)
    end = time.perf_counter()

    print("Execution time:", (end - start) * 1000, "milliseconds")
    print("Result shape:", C.shape)