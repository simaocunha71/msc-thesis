package main

import (
	"fmt"
)

func main() {
	fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4}))
}

func RemoveDuplicates(numbers []int) []int {
	seen := make(map[int]bool)
	result := []int{}
	for _, num := range numbers {
		if _, ok := seen[num]; !ok {
			seen[num] = true
			result = append(result, num)
		}
	}
	return result
}

func main() {
	fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4}))
}

func RemoveDuplicates(numbers []int) []int {
	seen := make(map[int]bool)
	result := []int{}
	for _, num := range numbers {
		if _, ok := seen[num]; !ok {
			seen[num] = true
			result = append(result, num)
		}
	}
	return result
}