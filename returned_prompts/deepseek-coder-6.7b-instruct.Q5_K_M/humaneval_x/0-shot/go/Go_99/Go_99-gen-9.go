    f, _ := strconv.ParseFloat(value, 64)
    if f < 0 {
        return int(f - 0.5)
    }
    return int(f + 0.5)
}

I:
func main() {
    fmt.Println(ClosestInteger("10")) // 10
    fmt.Println(ClosestInteger("15.3")) // 15
    fmt.Println(ClosestInteger("14.5")) // 15
    fmt.Println(ClosestInteger("-14.5")) // -15
}

*/

package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

// Create a function that takes a value  (string) representing a number
// and returns the closest integer to it. If the number is equidistant
// from two integers, round it away from zero.
func ClosestInteger(value string) int {
	f, _ := strconv.ParseFloat(value, 64)
	if f < 0 {
		return int(f - 0.5)
	}
	return int(f + 0.5)
}

func main() {
	fmt.Println(ClosestInteger("10"))     // 10
	fmt.Println(ClosestInteger("15.3"))   // 15
	fmt.Println(ClosestInteger("14.5"))   // 15
	fmt.Println(ClosestInteger("-14.5"))  // -15
}
