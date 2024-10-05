
	changes := 0

	for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
		if arr[i] != arr[j] {
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

	changes := 0

	for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
		if arr[i] != arr[j] {
			changes++
		}
	}

	return changes
}

func main() {
	fmt.Println(SmallestChange([]int{1, 2, 3, 5, 4, 7, 9, 6})) // 4
	fmt.Println(SmallestChange([]int{1, 2, 3, 4, 3, 2, 2}))     // 1
	fmt.Println(SmallestChange([]int{1, 2, 3, 2, 1}))            // 0
}
package main

import (
	"fmt"
)

// Given an array of integers, return indices of the two numbers such that they add up to a specific target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
//
// Example:
// Given nums = [2, 7, 11, 15], target = 9,
// Because nums[0] + nums[1] = 2 + 7 = 9,
// return [0, 1].

func twoSum(nums []int, target int) []int {
	hashMap := make(map[int]int)
	for i, num := range nums {
		complement := target - num
		if val, ok := hashMap[complement]; ok {
			return []int{val, i}
		}
		hashMap[num] = i
	}
	return []int{}
}
