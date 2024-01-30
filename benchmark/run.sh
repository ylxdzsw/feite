set -x

julia OMEinsum.jl $@
python np.py $@
python pytorch.py $@
