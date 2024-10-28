    if len(lst) == 0 {
        return 0
    }

B:
    sum := 0.0

C:
    for _, num := range lst {
        if num < 0 || math.Mod(num, 1) != 0 {
            continue
        }
        if math.Mod(num, 2) != 0 {
            sum += math.Pow(num, 2)
        }
    }

D:
    return int(sum)
}

*/

// Given a list of numbers, return the sum of squares of the numbers
// in the list that are odd. Ignore numbers that are negative or not integers.
//
// DoubleTheDifference([1, 3, 2, 0]) == 1 + ƒ(3) + ƒ(2) + ƒ(0) = 10
// DoubleTheDifference([-1, -2, 0]) == ƒ(-1) + ƒ(-2) + ƒ(0) = 0
// DoubleTheDifference([9, -2]) == 9 + ƒ(-2) = 81
// DoubleTheDifference([0]) == 0
//
// If the input list is empty, return 0.
func DoubleTheDifference(lst []float64) int {

	if len(lst) == 0 {
		return 0
	}

	sum := 0.0

	for _, num := range lst {
		if num < 0 || math.Mod(num, 1) != 0 {
			continue
		}
		if math.Mod(num, 2) != 0 {
			sum += math.Pow(num, 2)
		}
	}

	return int(sum)
}
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(DoubleTheDifference([]float64{1, 3, 2, 0}))
	fmt.Println(DoubleTheDifference([]float64{-1, -2, 0}))
	fmt.Println(DoubleTheDifference([]