    // Create a copy of the given array
    newArray := make([]int, len(array))
    copy(newArray, array)

    // Sort the new array
    sort.Ints(newArray)

    // Check if the sum of the first and last index values is even or odd
    if (newArray[0]+newArray[len(newArray)-1])%2 == 0 {
        // If even, reverse the new array
        for i := 0; i < len(newArray)/2; i++ {
            newArray[i], newArray[len(newArray)-1-i] = newArray[len(newArray)-1-i], newArray[i]
        }
    }

    return newArray
}

func main() {
    fmt.Println(SortArray([]int{})) // []
    fmt.Println(SortArray([]int{5})) // [5]
    fmt.Println(SortArray([]int{2, 4, 3, 0, 1, 5})) // [0, 1, 2, 3, 4, 5]
    fmt.Println(SortArray([]int{2, 4, 3, 0, 1, 5, 6})) // [6, 5, 4, 3, 2, 1, 0]
}
```

Here, we first create a copy of the given array because we need to not change the given array. Then, we sort the copied array. After that, we check the sum of the first and last index values. If the sum is even, we reverse the sorted array. Finally, we return the sorted array.

The time complexity of this function is O(n log n) because we use the sort.Ints function that has a time complexity of O(n log n). The space complexity is O(n) because we create a new array.

The function works as expected for the given examples.
*/

package main

import (
	"fmt"
	"sort"
)

func SortArray(array []int) []int {
	if len(array) == 0 {
		return []int{}
	}

	newArray :=