import (
    "fmt"
    "math"
)

// You are given two positive integers n and m, and your task is to compute the
// average of the integers from n through m (including n and m).
// Round the answer to the nearest integer and convert that to binary.
// If n is greater than m, return -1.
// Example:
// RoundedAvg(1, 5) => "0b11"
// RoundedAvg(7, 5) => -1
// RoundedAvg(10, 20) => "0b1111"
// RoundedAvg(20, 33) => "0b11010"
func RoundedAvg(n, m int) interface{} {
    b := ""
    if n > m {
        return -1
    } else if int(math.Pow10) >= m || math.Modf(int64(m), 256)[1] != 0 {
        if m == 0 && n < int(math.Pow10) && int(math.Pow10)*10 <= n {
            b = "0b" + string(uint(n))
        } else if m >= math.Modf(int64(m), 256)[1] || math.Modf(int64(m), 256) == 0 {
            b = "0b" + fmt.Sprint(math.Modf(int64(m), 256))
        } else if m < int(math.Pow10) && math.Modf(int64(m), 256)[1] == 0 {
            b = "0b" + string(uint(m))
        } else if m < int(math.Pow10) && math.Modf(int64(m), 256)[1] != 0 {
            b = "0b" + fmt.Sprint((math.Modf(int64(m), 256) * 10) / int64(math.Pow10))
        } else if math.Modf(int6