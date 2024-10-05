
// sort the array
sort.Ints(arr)

B:

// iterate over the array from the second to the last element
for i := 1; i < len(arr); i++ {

C:

// if the current element is not greater than the previous one
if arr[i] < arr[i-1] {

D:

// return the index of this element
return i
}
}

E:

// if no such element was found, return -1
return -1
}

*/

package main

import (
	"fmt"
	"sort"
)

func CanArrange(arr []int) int {
	// sort the array
	sort.Ints(arr)
	// iterate over the array from the second to the last element
	for i := 1; i < len(arr); i++ {
		// if the current element is not greater than the previous one
		if arr[i] < arr[i-1] {
			// return the index of this element
			return i
		}
	}
	// if no such element was found, return -1
	return -1
}

func main() {
	fmt.Println(CanArrange([]int{1, 2, 4, 3, 5}))
	fmt.Println(CanArrange([]int{1, 2, 3}))
}
/*

