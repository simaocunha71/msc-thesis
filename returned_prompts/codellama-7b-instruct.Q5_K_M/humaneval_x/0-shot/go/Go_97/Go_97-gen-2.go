import (
    "math"
)

// Complete the function that takes two integers and returns
// the product of their unit digits.
// Assume the input is always valid.
// Examples:
// Multiply(148, 412) should return 16.
// Multiply(19, 28) should return 72.
// Multiply(2020, 1851) should return 0.
// Multiply(14,-15) should return 20.
func Multiply(a, b int) int {
    return int(math.Mod(float64(a%10*b%10), 10))
}
