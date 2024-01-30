import numpy as np
import time
import sys

np.random.seed(3)

code = sys.argv[1]
shape_dict = {
    x[0]: int(x[1:])
    for x in sys.argv[2:]
}

inputs = []
input_codes, output_code = code.split("->")
for input_code in input_codes.split(","):
    input_shape = [shape_dict[c] for c in input_code]
    inputs.append(np.random.rand(*input_shape).astype(np.float32))

time1 = time.time_ns()

path = np.einsum_path(code, *inputs, optimize="optimal")[0]

time2 = time.time_ns()

np.einsum(code, *inputs, optimize=path)

time3 = time.time_ns()

np.einsum(code, *inputs, optimize=path)

time4 = time.time_ns()

np.einsum(code, *inputs, optimize=path)

time5 = time.time_ns()

print(f"Compile time: {(time2 - time1) / 1e6:.10f}")
print(f"First run time: {(time3 - time2) / 1e6:.10f}")
print(f"Second run time: {(time4 - time3) / 1e6:.10f}")
print(f"Third run time: {(time5 - time4) / 1e6:.10f}")
