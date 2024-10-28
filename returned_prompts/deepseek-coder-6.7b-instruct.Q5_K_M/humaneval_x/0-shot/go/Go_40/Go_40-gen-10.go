
// Start by initializing a counter to keep track of the number of triples that sum to zero.
counter := 0

// Next, iterate over the list of integers.
for i := 0; i < len(l); i++ {

// For each integer, iterate over the remaining elements of the list.
for j := i + 1; j < len(l); j++ {

// For each pair of integers, iterate over the remaining elements of the list.
for k := j + 1; k < len(l); k++ {

// If the sum of the current triple is zero, increment the counter.
if l[i] + l[j] + l[k] == 0 {
counter++
}
}
}
}

// If the counter is greater than zero, return true, otherwise return false.
if counter > 0 {
return true
} else {
return false
}
}

*/

package main

import "fmt"

func TriplesSumToZero(l []int) bool {
	counter := 0
	for i := 0; i < len(l); i++ {
		for j := i + 1; j < len(l); j++ {
			for k := j + 1; k < len(l); k++ {
				if l[i]+l[j]+l[k] == 0 {
					counter++
				}
			}
		}
	}
	if counter > 0 {
		return true
	} else {
		return false
	}
}

func main() {
	fmt.Println(TriplesSumToZero([]int{1, 3, 5, 0}))
	fmt.Println(TriplesSumToZero([]int{1, 3, -2, 1}))
	fmt.Println(TriplesSumToZero([]int{1, 2, 3, 7}))
	fmt.Println(TriplesSumToZero([]int{2, 4, -5, 3, 9, 7}))
	fmt.Println(TriplesSumToZero([]int{1}))
}
/*
