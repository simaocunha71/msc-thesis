
// Your task is to write a function that returns true if a number x is a
// simple power of n and false in other cases.
// x is a simple power of n if n**int=x
// For example:
// IsSimplePower(1, 4) => true
// IsSimplePower(2, 2) => true
// IsSimplePower(8, 2) => true
// IsSimplePower(3, 2) => false
// IsSimplePower(3, 1) => false
// IsSimplePower(5, 3) => false
func IsSimplePower(x int,n int) bool {
    y := math.Log(float64(x)) / math.Log(float64(n))
    return math.Pow(float64(n), y) == float64(x)
}

