
	n := len(arr)
	changes := 0
	
	for i := 0; i < n/2; i++ {
		if arr[i] != arr[n-i-1] {
			changes++
		}
	}
	
	return changes
}

*/
package main

import (
	"fmt"
)

func SmallestChange(arr []int) int {

	n := len(arr)
	changes := 0

	for i := 0; i < n/2; i++ {
		if arr[i] != arr[n-i-1] {
			changes++
		}
	}

	return changes
}

func main() {
	fmt.Println(SmallestChange([]int{1, 2, 3, 5, 4, 7, 9, 6})) // 4
	fmt.Println(SmallestChange([]int{1, 2, 3, 4, 3, 2, 2}))      // 1
	fmt.Println(SmallestChange([]int{1, 2, 3, 2, 1}))             // 0
}
/*
