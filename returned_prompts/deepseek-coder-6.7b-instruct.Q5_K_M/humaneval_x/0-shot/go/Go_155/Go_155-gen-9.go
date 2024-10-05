    var count [2]int
    numStr := strconv.Itoa(num)
    for _, ch := range numStr {
        digit, _ := strconv.Atoi(string(ch))
        if digit % 2 == 0 {
            count[0]++
        } else {
            count[1]++
        }
    }
    return count
}

*/

package main

import (
	"fmt"
	"strconv"
)

func EvenOddCount(num int) [2]int {
	var count [2]int
	numStr := strconv.Itoa(num)
	for _, ch := range numStr {
		digit, _ := strconv.Atoi(string(ch))
		if digit%2 == 0 {
			count[0]++
		} else {
			count[1]++
		}
	}
	return count
}

func main() {
	fmt.Println(EvenOddCount(-12)) // ==> [1, 1]
	fmt.Println(EvenOddCount(123)) // ==> [1, 2]
}
package main

import (
	"fmt"
	"math"
	"sort"
)

func MinDistanceToZero(arr []int) int {
	sort.Ints(arr)
	return arr[0]
}

func main() {
	// Test the function
	arr := []int{3, -2, 1, 4, -5, 6}
	fmt.Println(MinDistanceToZero(arr)) // Output: -5
}

// alternative solution
// func MinDistanceToZero(arr []int) int {
// 	min := math.MaxInt64
// 	for _, num := range arr {
// 		if num < 0 && -num < min {
// 			min = -num
// 		} else if num > 0 && num < min {
// 			min = num
// 		}
// 	}
// 	return min
// }

// alternative solution
// func MinDistanceToZero(arr []int)