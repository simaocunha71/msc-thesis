package main

import (
	"fmt"
	"math"
)

func LargestSmallestIntegers(lst []int) [2]interface{} {
	max := math.Inf(-1)
	min := math.Inf(1)

	for _, num := range lst {
		if num < 0 && num > max {
			max = num
		}
		if num > 0 && num < min {
			min = num
		}
	}

	return [2]interface{}{max, min}
}

func main() {
	fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7}))   // (nil, 1)
	fmt.Println(LargestSmallestIntegers([]int{}))                 // (nil, nil)
	fmt.Println(LargestSmallestIntegers([]int{0}))                // (nil, nil)
	fmt.Println(LargestSmallestIntegers([]int{-10, -20, -30}))    // (-10, -30)
	fmt.Println(LargestSmallestIntegers([]int{10, 20, 30}))       // (10, 20)
	fmt.Println(LargestSmallestIntegers([]int{-10, 20, -30, 40})) // (-10, 20)
}