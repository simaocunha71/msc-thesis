    copyArray := make([]int, len(array))
    copy(copyArray, array)
    if len(array) > 1 {
        if (array[0] + array[len(array)-1]) % 2 == 0 {
            sort.Sort(sort.Reverse(sort.IntSlice(copyArray)))
        } else {
            sort.Ints(copyArray)
        }
    }
    return copyArray
}

func main()  {
    fmt.Println(SortArray([]int{})) // []
    fmt.Println(SortArray([]int{5})) // [5]
    fmt.Println(SortArray([]int{2, 4, 3, 0, 1, 5})) // [0, 1, 2, 3, 4, 5]
    fmt.Println(SortArray([]int{2, 4, 3, 0, 1, 5, 6})) // [6, 5, 4, 3, 2, 1, 0]
}

*/
package main

import (
	"fmt"
	"sort"
)

func SortArray(array []int) []int {

	copyArray := make([]int, len(array))
	copy(copyArray, array)
	if len(array) > 1 {
		if (array[0]+array[len(array)-1])%2 == 0 {
			sort.Sort(sort.Reverse(sort.IntSlice(copyArray)))
		} else {
			sort.Ints(copyArray)
		}
	}
	return copyArray
}

func main() {
	fmt.Println(SortArray([]int{}))                              // []
	fmt.Println(SortArray([]int{5}))                             // [5]
	fmt.Println(SortArray([]int{2, 4, 3, 0, 1, 5}))             // [0, 1, 2, 3, 4, 5]
	fmt.Println(SortArray([]int{2, 4, 3, 0, 1,