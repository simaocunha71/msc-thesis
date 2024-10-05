
	positive := []int{}
	for _, num := range l {
		if num > 0 {
			positive = append(positive, num)
		}
	}
	return positive
}

*/

package main

import "fmt"

func GetPositive(l []int) []int {

	positive := []int{}
	for _, num := range l {
		if num > 0 {
			positive = append(positive, num)
		}
	}
	return positive
}

func main() {
	fmt.Println(GetPositive([]int{-1, 2, -4, 5, 6}))
	fmt.Println(GetPositive([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))
}
package main

import (
	"fmt"
	"math"
)

func Round(input float64) float64 {
	return math.Round(input/0.5) * 0.5
}

func main() {
	fmt.Println(Round(1.2))  // Output: 1
	fmt.Println(Round(1.5))  // Output: 2
	fmt.Println(Round(2.5))  // Output: 2
	fmt.Println(Round(3.5))  // Output: 4
	fmt.Println(Round(4.5))  // Output: 4
	fmt.Println(Round(5.5))  // Output: 6
	fmt.Println(Round(6.5))  // Output: 6
	fmt.Println(Round(7.5))  // Output: 8
	fmt.Println(Round(8.5))  // Output: 8
	fmt.Println(Round(9.5))  // Output: 10
	fmt.Println(Round(10.5)) // Output: 10
	fmt.Println(Round(11.5)) // Output: 12
}

/*