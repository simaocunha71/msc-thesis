
    // your code
    
}

*/

package main

import (
	"fmt"
	"math"
)

func Intersection(interval1 [2]int, interval2 [2]int) string {
	start := int(math.Max(float64(interval1[0]), float64(interval2[0])))
	end := int(math.Min(float64(interval1[1]), float64(interval2[1])))

	if start > end {
		return "NO"
	}

	length := end - start + 1
	isPrime := true

	if length == 1 || length%2 == 0 {
		isPrime = false
	} else {
		for i := 3; i*i <= length; i += 2 {
			if length%i == 0 {
				isPrime = false
				break
			}
		}
	}

	if isPrime {
		return "YES"
	}

	return "NO"
}

func main() {
	fmt.Println(Intersection([2]int{1, 2}, [2]int{2, 3}))
	fmt.Println(Intersection([2]int{-1, 1}, [2]int{0, 4}))
	fmt.Println(Intersection([2]int{-3, -1}, [2]int{-5, 5}))
}

// func Intersection(interval1 [2]int, interval2 [2]int) string {
// 	start := int(math.Max(float64(interval1[0]), float64(interval2[0])))
// 	end := int(math.Min(float64(interval1[1]), float64(interval2[1])))

// 	if start > end {
// 		return "NO"
// 	}

// 	length := end - start + 1
// 	if length == 1 || length%2 == 0 {
// 		return "NO"
// 	}

// 	for i := 3; i*i <= length; i += 2 {
// 		if length%