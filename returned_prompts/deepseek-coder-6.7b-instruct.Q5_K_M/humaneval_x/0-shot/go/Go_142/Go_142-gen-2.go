    sum := 0
    for i, v := range lst {
        if i%3 == 0 {
            sum += int(math.Pow(float64(v), 2))
        } else if i%4 == 0 {
            sum += int(math.Pow(float64(v), 3))
        } else {
            sum += v
        }
    }
    return sum
}

*/

package main

import (
	"fmt"
	"math"
)

func SumSquares(lst []int) int {
	sum := 0
	for i, v := range lst {
		if i%3 == 0 {
			sum += int(math.Pow(float64(v), 2))
		} else if i%4 == 0 {
			sum += int(math.Pow(float64(v), 3))
		} else {
			sum += v
		}
	}
	return sum
}

func main() {
	fmt.Println(SumSquares([]int{1, 2, 3}))
	fmt.Println(SumSquares([]int{}))
	fmt.Println(SumSquares([]int{-1, -5, 2, -1, -5}))
}

// Output:
// 9
// 0
// -126
// Explanation:
// For lst 1,2,3: the numbers at indices 0 and 3 are multiples of 3, so we square them (1^2 and 3^2). The sum is 1^2 + 3^2 = 9.
// For lst (empty): the sum is 0 because there are no elements to sum.
// For lst -1,-5,2,-1,-5: the numbers at indices 0, 1, and 4 are multiples of 3 (and the number at index 4 is also a multiple of 4), so we square them (1^2, 5^2 and 5^2). The sum is 1^2 + 5^2 + 5^2 = -126.
