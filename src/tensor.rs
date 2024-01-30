pub struct Tensor {
    pub ptr: *const f32,
    pub shape: Vec<usize>,
    pub strides: Vec<usize>, // number of elements to skip to get to the next element in each dimension
}

impl Tensor {
    pub fn new(ptr: *const f32, shape: Vec<usize>, strides: Vec<usize>) -> Self {
        Self {
            ptr,
            shape,
            strides,
        }
    }
}
