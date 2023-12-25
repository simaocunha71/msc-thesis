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
    if a == 0 || b == 0 {
        return 0;
    }
    // 10^x can be calculated with x bit shift operation:
    // multiply by 10 and add to unit digit.
    // For example, the value of "5" in binary form is:
    //   b32 = 0b101101111, or (1 << 4) + 5 + ((-1) << 3).
    if a > 9 {
        return math.Pow(int(math.Pow(10, int(a))), int(b))
    } else {
        return math.Pow(int(math.Pow(10, int(b))), (int)(-1) << 3) + a;
    }
}