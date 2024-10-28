    sort.Ints(nums)
    n := len(nums)
    sum := 0
    for i:=0; i<n; i+=2 {
        sum += nums[i]
    }
    return sum
}

In this code, we first sort the given array of integers nums in increasing order. Then, we iterate through the array in steps of 2 (starting from index 0) adding the current element to the sum. This way, we cover all the elements of the array with the minimum sum. Finally, we return the sum.

The reason why this works is that the array is sorted in increasing order, so we always add the smallest possible number to the sum. This way, we end up with the smallest possible sum of any non-empty sub-array of nums.
*/
package main

import (
	"fmt"
	"sort"
)

func Minsubarraysum(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	sum := 0
	for i := 0; i < n; i += 2 {
		sum += nums[i]
	}
	return sum
}

func main() {
	fmt.Println(Minsubarraysum([]int{2, 3, 4, 1, 2, 4})) // Expected output: 1
	fmt.Println(Minsubarraysum([]int{-1, -2, -3}))         // Expected output: -6
}

/*
