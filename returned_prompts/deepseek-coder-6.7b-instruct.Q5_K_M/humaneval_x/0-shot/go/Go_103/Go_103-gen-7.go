    if n > m {
        return -1
    }
B:
    avg := math.Round(float64(n+m) / 2)
C:
    binary := fmt.Sprintf("%b", int(avg))
    return binary
}

func main() {
    fmt.Println(RoundedAvg(1, 5)) // => "0b11"
    fmt.Println(RoundedAvg(7, 5)) // => -1
    fmt.Println(RoundedAvg(10, 20)) // => "0b1111"
    fmt.Println(RoundedAvg(20, 33)) // => "0b11010"
}


A: If n is greater than m, then return -1.
B: Compute the average of n and m (rounded to the nearest integer), and store the result in avg.
C: Convert avg to a binary string and return it.

*/

package main

import (
	"fmt"
	"math"
)

func RoundedAvg(n, m int) interface{} {
	if n > m {
		return -1
	}
	avg := math.Round(float64(n+m) / 2)
	binary := fmt.Sprintf("%b", int(avg))
	return binary
}

func main() {
	fmt.Println(RoundedAvg(1, 5))  // => "0b11"
	fmt.Println(RoundedAvg(7, 5))  // => -1
	fmt.Println(RoundedAvg(10, 20)) // => "0b1111"
	fmt.Println(RoundedAvg(20, 33)) // => "0b11010"
}
