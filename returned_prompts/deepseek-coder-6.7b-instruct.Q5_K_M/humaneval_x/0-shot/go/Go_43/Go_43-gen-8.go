
	sort.Ints(l)

B:

	for i := 0; i < len(l) - 1; i++ {
		j := sort.SearchInts(l[i+1:], -l[i])
		if j != len(l[i+1:]) && l[i] != 0 {
			return true
		}
	}
	return false
}




*/

/*

PairsSumToZero takes a list of integers as an input.
It returns true if there are two distinct elements in the list that
sum to zero, and false otherwise.
>>> PairsSumToZero([1, 3, 5, 0])
false
>>> PairsSumToZero([1, 3, -2, 1])
false
>>> PairsSumToZero([1, 2, 3, 7])
false
>>> PairsSumToZero([2, 4, -5, 3, 5, 7])
true
>>> PairsSumToZero([1])
false

*/

package main

import (
	"fmt"
	"sort"
)

func PairsSumToZero(l []int) bool {

	sort.Ints(l)

	for i := 0; i < len(l)-1; i++ {
		j := sort.SearchInts(l[i+1:], -l[i])
		if j != len(l[i+1:]) && l[i] != 0 {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(PairsSumToZero([]int{1, 3, 5, 0}))         // false
	fmt.Println(PairsSumToZero([]int{1, 3, -2, 1}))        // false
	fmt.Println(PairsSumToZero([]int{1, 2, 3, 7}))         // false
	fmt.Println(PairsSumToZero([]int{2, 4, -5, 3, 5, 7})) // true
	fmt.Println(