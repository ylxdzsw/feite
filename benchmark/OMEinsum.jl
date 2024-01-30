using Random
Random.seed!(3)

using OMEinsum

code = ARGS[1]
shape_dict = Dict(
    x[1] => parse(Int, x[2:end])
    for x in ARGS[2:end]
)

inputs = []
input_codes, output_code = split(code, "->")
for input_code in split(input_codes, ",")
    input_shape = [shape_dict[c] for c in input_code]
    push!(inputs, rand(Float32, input_shape...))
end

time1 = time_ns()

code = @eval @ein_str $code
optcode = optimize_code(code, shape_dict, TreeSA())

run = let inputs = inputs, optcode = optcode
    () -> optcode(inputs...)
end

time2 = time_ns()

run()

time3 = time_ns()

run()

time4 = time_ns()

run()

time5 = time_ns()

println("Compile time: ", (time2 - time1) / 1e6)
println("First run time: ", (time3 - time2) / 1e6)
println("Second run time: ", (time4 - time3) / 1e6)
println("Third run time: ", (time5 - time4) / 1e6)
