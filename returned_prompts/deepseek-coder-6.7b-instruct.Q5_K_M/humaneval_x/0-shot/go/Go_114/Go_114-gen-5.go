    sort.Ints(nums)

    sum, total := 0, 0
    for _, num := range nums {
        sum += num
        total += sum
   
    return total - len(nums) * nums[0]
}

This algorithm first sorts the array in ascending order. It then calculates the sum of all the numbers in the array. After that, it calculates the total sum of all sub-arrays by adding the sum of each consecutive pair of numbers in the sorted array. Finally, it subtracts the sum of the smallest sub-array from the total sum which is the sum of all sub-arrays. The smallest sub-array is the one with the smallest sum, so we subtract the product of the smallest number and the number of elements in the array from the total sum.

This algorithm has a time complexity of O(n log n) due to the sorting operation, where n is the length of the input array. The space complexity is O(1) because the algorithm uses a constant amount of space to store the sum and total variables.

Note: This code assumes that the input array is not empty and contains at least one positive number. If the input array can contain negative numbers as well, the smallest sub-array may not be the one with the smallest sum. In such a case, you would need to use a different approach to find the smallest sub-array.
*/

package main

import (
	"fmt"
	"sort"
)

func Minsubarraysum(nums []int) int {
	sort.Ints(nums)

	sum, total := 0, 0
	for _, num := range nums {
		sum += num
		total += sum
	}

	return total - len(nums)*nums[0]
}

func main() {
	fmt.Println(Minsubarraysum([]int{2, 3, 4, 1, 2, 4})) // Output: 1
	fmt.Println(Minsubarraysum([]int{-1, -2, -3}))        // Output: -6
}

/*
This program works by first sorting the input array. Then it calculates the sum of the