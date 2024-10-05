    if n > m {
        return -1
    }
B:
    avg := math.Round(float64(n+m) / 2)
C:
    binary := fmt.Sprintf("%b", int(avg))
D:
    return binary
}

// The function RoundedAvg computes the average of the integers from n through m,
// rounds the answer to the nearest integer, converts it to binary, and returns it.
// If n is greater than m, the function returns -1.
func main() {

E:
    fmt.Println(RoundedAvg(1, 5)) // "0b11"
F:
    fmt.Println(RoundedAvg(7, 5)) // -1
G:
    fmt.Println(RoundedAvg(10, 20)) // "0b1111"
H:
    fmt.Println(RoundedAvg(20, 33)) // "0b11010"
}

// This program uses the math and fmt packages to compute the average of the numbers,
// round it to the nearest integer, convert it to binary, and print the result.
// If n is greater than m, the program prints -1.
func main() {

I:
    fmt.Println(RoundedAvg(1, 5)) // "0b11"
J:
    fmt.Println(RoundedAvg(7, 5)) // -1
K:
    fmt.Println(RoundedAvg(10, 20)) // "0b1111"
L:
    fmt.Println(RoundedAvg(20, 33)) // "0b11010"
}

// This program uses the math and fmt packages to compute the average of the numbers,
// round it to the nearest integer, convert it to binary, and print the result.
// If n is greater than m, the program prints -1.

*/

package main

import (
	"fmt"
	"math"
)

func RoundedAvg(n, m int) interface{} {
