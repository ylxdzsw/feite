import torch
import time
import sys

# torch.backends.opt_einsum.strategy = 'optimal'

torch.manual_seed(3)

code = sys.argv[1]
shape_dict = {
    x[0]: int(x[1:])
    for x in sys.argv[2:]
}

inputs = []
input_codes, output_code = code.split("->")
for input_code in input_codes.split(","):
    input_shape = [shape_dict[c] for c in input_code]
    inputs.append(torch.rand(*input_shape).float())

time1 = time.time_ns()

torch.einsum(code, *inputs)

time2 = time.time_ns()

torch.einsum(code, *inputs)

time3 = time.time_ns()

torch.einsum(code, *inputs)

time4 = time.time_ns()

print(f"First run time: {(time2 - time1) / 1e6:.10f}")
print(f"Second run time: {(time3 - time2) / 1e6:.10f}")
print(f"Third run time: {(time4 - time3) / 1e6:.10f}")
