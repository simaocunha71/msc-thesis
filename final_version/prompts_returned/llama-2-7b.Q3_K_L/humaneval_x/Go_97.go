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
    if a == -1 || b == -1 {
        return math.MinInt32 + math.MaxInt32
    } else if a != 0 && b != 0 {
        ndigit := (10 * a / b) % 10
        return int(math.Pow(10, -ndigit))*int(a/b)+(9-ndigit)/2
    } else if a == 0 && b != 0 {
        ndigit := (10 * b / a) % 10
        return int(math.Pow(10, -ndigit))*int(a/b)+(9-ndigit)/2
    } else if a == 0 && b == 0 {
        ndigit := 9
        return int(math.Pow(10, -ndigit))+int(10*math.Log10(float64((a+b))))
    } else {
        panic("invalid input")
    }
}
