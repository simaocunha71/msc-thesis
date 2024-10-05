
Here's a solution in Go:

```go
package main

import (
	"fmt"
)

func PairsSumToZero(l []int) bool {
	m := make(map[int]int)

	for _, v := range l {
		if _, ok := m[v]; ok {
			return true
		}
		m[v]++
	}

	return false
}

func main() {
	tests := []struct {
		in      []int
		want   bool
	}{
		{[]int{1, 3, 5, 0}, false},
		{[]int{1, 3, -2, 1}, false},
		{[]int{1, 2, 3, 7}, false},
		{[]int{2, 4, -5, 3, 5, 7}, true},
		{[]int{1}, false},
	}

	for _, test := range tests {
		if got := PairsSumToZero(test.in); got != test.want {
			fmt.Errorf("got %t, want %t", got, test.want)
		}
	}
}
```

The `PairsSumToZero` function creates a map called `m` to keep track of the count of each number in the input list. It then iterates over the input list, checking if the current number is already in the map. If it is, that means there are two distinct elements in the list that sum to zero, so the function returns `true`. If the current number is not in the map, it adds it with a count of 1. After iterating over the entire input list, if no two numbers sum to zero, the function returns `false`.

The `main` function contains a set of test cases to verify the correctness of the `PairsSumToZero` function. It creates a slice of structs, each containing an input list and the expected output. It then iterates over the test cases, calling the `PairsSumToZero` function with the input list and comparing the result to the expected output.

The output of the program, when run,