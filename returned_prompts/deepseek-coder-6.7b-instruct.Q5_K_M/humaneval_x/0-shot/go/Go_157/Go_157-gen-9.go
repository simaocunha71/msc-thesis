
// Your code here
}

*/

package main

import (
	"fmt"
	"sort"
)

func RightAngleTriangle(a, b, c int) bool {

	arr := []int{a, b, c}
	sort.Ints(arr)

	return arr[0]*arr[0]+arr[1]*arr[1] == arr[2]*arr[2]
}

func main() {
	fmt.Println(RightAngleTriangle(3, 4, 5)) // true
	fmt.Println(RightAngleTriangle(1, 2, 3)) // false
}
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(Max(3, 6, 9)) // 9
	fmt.Println(Max(3, -6, 9)) // 9
	fmt.Println(Max(3, 0, 9)) // 9
	fmt.Println(Max(-3, -6, -9)) // -3
}

// Max returns the maximum value among the given numbers.
func Max(nums ...float64) float64 {
	max := math.Inf(-1)
	for _, num := range nums {
		if num > max {
			max = num
		}
	}
	return max
}

// Min returns the minimum value among the given numbers.
func Min(nums ...float64) float64 {
	min := math.Inf(1)
	for _, num := range nums {
		if num < min {
			min = num
		}
	}
	return min
}

// Avg calculates the average of given numbers.
func Avg(nums ...float64) float64 {
	sum := 0.0
	for _, num := range nums {
		sum += num
	}
	return sum / float64(len(nums))
}

// Sum calculates the sum of given numbers.
func Sum(nums ...float64) float64 {
	sum :