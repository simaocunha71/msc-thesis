    if n > m {
        return -1
    }

B:
    avg := int(math.Round(float64(n+m) / 2))

C:
    return fmt.Sprintf("0b%b", avg)
}

func main() {
    fmt.Println(RoundedAvg(1, 5)) // => "0b11"
    fmt.Println(RoundedAvg(7, 5)) // => -1
    fmt.Println(RoundedAvg(10, 20)) // => "0b1111"
    fmt.Println(RoundedAvg(20, 33)) // => "0b11010"
}

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

	avg := int(math.Round(float64(n+m) / 2))

	return fmt.Sprintf("0b%b", avg)
}

func main() {
	fmt.Println(RoundedAvg(1, 5))   // => "0b11"
	fmt.Println(RoundedAvg(7, 5))   // => -1
	fmt.Println(RoundedAvg(10, 20)) // => "0b1111"
	fmt.Println(RoundedAvg(20, 33)) // => "0b11010"
}

// This program calculates the rounded average of two given integers and converts it to binary. If the first number is greater than the second one, the function returns -1.
// The function RoundedAvg takes two integers as arguments, calculates the rounded average of the numbers, converts the average to binary format and returns it as a string.
// The main function demonstrates the usage of this function with a few examples.
// The function works by first checking if the first number is greater than the second one. If it is, the function returns -1.
// Otherwise,