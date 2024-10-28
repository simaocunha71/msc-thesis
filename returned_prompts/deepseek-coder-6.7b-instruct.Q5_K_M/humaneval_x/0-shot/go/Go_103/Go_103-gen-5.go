    if n > m {
        return -1
    }
B:
    avg := math.Round(float64(n+m) / 2)
C:
    return fmt.Sprintf("%b", int(avg))
}

func main() {
    fmt.Println(RoundedAvg(1, 5))  // 0b11
    fmt.Println(RoundedAvg(7, 5))  // -1
    fmt.Println(RoundedAvg(10, 20))  // 0b1111
    fmt.Println(RoundedAvg(20, 33))  // 0b11010
}

*/
package main

import (
	"fmt"
	"math"
)

// You are given two positive integers n and m, and your task is to compute the
// average of the integers from n through m  (including n and m).
// Round the answer to the nearest integer and convert that to binary.
// If n is greater than m, return -1.
// Example:
// RoundedAvg(1, 5) => “0b11”
// RoundedAvg(7, 5) → -1
// RoundedAvg(10, 20) → “0b1111”
// RoundedAvg(20, 33) → “0b11010”
func RoundedAvg(n, m int) interface{} {
	if n > m {
		return -1
	}
	avg := math.Round(float64(n+m) / 2)
	return fmt.Sprintf("%b", int(avg))
}

func main() {
	fmt.Println(RoundedAvg(1, 5))  // 0b11
	fmt.Println(RoundedAvg(7, 5))  // -1
	fmt.Println(RoundedAvg(10, 20))  // 0b1111
	fmt.Println(RoundedAvg(20, 33