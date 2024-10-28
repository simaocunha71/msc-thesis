
    // Sort the array in ascending order
    sort.Ints(arr)

B:

    // Iterate through the array
    for i := 0; i < len(arr) - 1; i++ {

C:

        // Check if the current element is not greater than or equal to the
        // next element
        if arr[i] < arr[i+1] {

D:

            // If it is not, return the current index
            return i
        }

E:

    }

F:

    // If no such element exists, return -1
    return -1

}

G:


func main() {
    fmt.Println(CanArrange([]int{1,2,4,3,5})) // 3
    fmt.Println(CanArrange([]int{1,2,3})) // -1
}

*/

// Create a function which returns the largest index of an element which
// is not greater than or equal to the element immediately preceding it. If
// no such element exists then return -1. The given array will not contain
// duplicate values.
func CanArrange(arr []int) int {

	// Sort the array in ascending order
	sort.Ints(arr)

	// Iterate through the array
	for i := 0; i < len(arr)-1; i++ {

		// Check if the current element is not greater than or equal to the
		// next element
		if arr[i] < arr[i+1] {

			// If it is not, return the current index
			return i
		}
	}

	// If no such element exists, return -1
	return -1
}

func main() {
	fmt.Println(CanArrange([]int{1, 2, 4, 3, 5})) // 3
	fmt.Println(CanArrange([]int{1, 2, 3}))        // -1
}
package main

import (
	"fmt"
)

/*
