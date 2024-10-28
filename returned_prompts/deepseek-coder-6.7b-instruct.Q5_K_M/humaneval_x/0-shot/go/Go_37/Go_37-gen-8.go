	even := make([]int, 0, len(l)/2)
	for i := 0; i < len(l); i += 2 {
		even = append(even, l[i])
	}

	sort.Ints(even)

	res := make([]int, len(l))
	for i := 0; i < len(l); i++ {
		if i%2 == 0 {
			res[i] = even[i/2]
		} else {
			res[i] = l[i]
		}
	}

	return res
}

*/

package main

import (
	"fmt"
	"sort"
)

func SortEven(l []int) []int {
	even := make([]int, 0, len(l)/2)
	for i := 0; i < len(l); i += 2 {
		even = append(even, l[i])
	}

	sort.Ints(even)

	res := make([]int, len(l))
	for i := 0; i < len(l); i++ {
		if i%2 == 0 {
			res[i] = even[i/2]
		} else {
			res[i] = l[i]
		}
	}

	return res
}

func main() {
	fmt.Println(SortEven([]int{1, 2, 3, 4})) // [1, 2, 3, 4]
	fmt.Println(SortEven([]int{5, 6, 3, 4})) // [3, 6, 5, 4]
}

/*

Output:
[1 2 3 4]
[3 6 5 4]

*/

/*

This code sorts the elements at even indices in the list, keeping the elements at odd indices the same. The sorted elements at even indices are then inserted back into the list at their original even indices.

The function `SortEven` takes a slice `l` of integers as input and returns a new slice `res` where the elements at even indices are the sorted