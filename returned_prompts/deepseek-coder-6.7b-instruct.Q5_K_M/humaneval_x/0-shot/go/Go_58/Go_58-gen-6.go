    var result []int

    m := make(map[int]bool)
    for _, item := range l1 {
        m[item] = true
    }

    for _, item := range l2 {
        if _, ok := m[item]; ok {
            result = append(result, item)
        }
    }

    sort.Ints(result)

    return result
}

*/

package main

import (
	"fmt"
	"sort"
)

func Common(l1 []int, l2 []int) []int {

	var result []int

	m := make(map[int]bool)
	for _, item := range l1 {
		m[item] = true
	}

	for _, item := range l2 {
		if _, ok := m[item]; ok {
			result = append(result, item)
		}
	}

	sort.Ints(result)

	return result
}

func main() {

	result := Common([]int{1, 4, 3, 34, 653, 2, 5}, []int{5, 7, 1, 5, 9, 653, 121})
	fmt.Println(result)

	result = Common([]int{5, 3, 2, 8}, []int{3, 2})
	fmt.Println(result)
}
/*

Create a function that takes an array of numbers and returns the second largest unique number in the array.

If there are no unique numbers, return None. If there is no second largest unique number, also return None.

Examples:

second_largest([10, 20, 40, 30, 20, 10]) ➞ 30

second_largest([25, 25, 25, 25, 25, 25]) ➞ None

second_largest([2, 2, 1]) ➞ 1

Notes:

    All inputs given in the array