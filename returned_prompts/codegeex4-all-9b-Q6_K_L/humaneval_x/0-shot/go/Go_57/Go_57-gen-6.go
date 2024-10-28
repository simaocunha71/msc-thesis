package main

import (
	"fmt"
)

func Monotonic(l []int) bool {
	if len(l) <= 1 {
		return true
	}

	increasing := false
	decreasing := false

	for i := 1; i < len(l); i++ {
		if l[i] > l[i-1] {
			increasing = true
		} else if l[i] < l[i-1] {
			decreasing = true
		}

		if increasing && decreasing {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(Monotonic([]int{1, 2, 4, 20})) // true
	fmt.Println(Monotonic([]int{1, 20, 4, 10})) // false
	fmt.Println(Monotonic([]int{4, 1, 0, -10})) // true
}

