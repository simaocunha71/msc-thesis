
The solution to the problem is as follows:

```go
package main

import (
	"fmt"
)

func TriplesSumToZero(l []int) bool {
	// Sort the list of numbers
	l = Sort(l)

	// Loop over all possible triplets of three distinct numbers
	for i := 0; i < len(l)-2; i++ {
		for j := i + 1; j < len(l)-1; j++ {
			for k := j + 1; k < len(l); k++ {
				if l[i]+l[j]+l[k] == 0 {
					return true
				}
			}
		}
	}
	return false
}

func main() {
	// Tests
	fmt.Println(TriplesSumToZero([]int{1, 3, 5, 0})) // false
	fmt.Println(TriplesSumToZero([]int{1, 3, -2, 1})) // true
	fmt.Println(TriplesSumToZero([]int{1, 2, 3, 7})) // false
	fmt.Println(TriplesSumToZero([]int{2, 4, -5, 3, 9, 7})) // true
	fmt.Println(TriplesSumToZero([]int{1})) // false
}
```

This function first sorts the input list, which is necessary because we need to check all possible triplets. Then, it checks all triplets of three distinct numbers in the list and returns true if it finds a triplet that sums to zero, and false otherwise.

The function is implemented as follows:

```go
func TriplesSumToZero(l []int) bool {
	// Sort the list of numbers
	l = Sort(l)

	// Loop over all possible triplets of three distinct numbers
	for i := 0; i < len(l)-2; i++ {
		for j := i + 1; j < len(l)-1; j++ {
			for k := j + 1; k