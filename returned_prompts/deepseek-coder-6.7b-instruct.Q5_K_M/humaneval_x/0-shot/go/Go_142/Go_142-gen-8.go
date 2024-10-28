    sum := 0
    for i, num := range lst {
        switch {
        case i%3 == 0:
            sum += int(math.Pow(float64(num), 2))
        case i%4 == 0:
            sum += int(math.Pow(float64(num), 3))
        default:
            sum += num
        }
    }
    return sum
}

*/

// SumSquares calculates the sum of square or cube of numbers in the list according to their indexes.
func SumSquares(lst []int) int {
	sum := 0
	for i, num := range lst {
		switch {
		case i%3 == 0:
			sum += int(math.Pow(float64(num), 2))
		case i%4 == 0:
			sum += int(math.Pow(float64(num), 3))
		default:
			sum += num
		}
	}
	return sum
}

func main() {
	lst := []int{1, 2, 3}
	fmt.Println(SumSquares(lst)) // Should print 6
	lst = []int{}
	fmt.Println(SumSquares(lst)) // Should print 0
	lst = []int{-1, -5, 2, -1, -5}
	fmt.Println(SumSquares(lst)) // Should print -126
}
package main

import (
	"fmt"
	"math"
)

// CalculateDistance calculates the distance between two points using the formula derived from the Pythagorean theorem.
func CalculateDistance(x1, y1, x2, y2 float64) float64 {
	return math.Sqrt(math.Pow(x2-x1, 2) + math.Pow(y2-y1, 2))
}

func main() {
	fmt.Println(CalculateDistance(2, 2, 5, 5)) // Should print 5
	fmt.Println