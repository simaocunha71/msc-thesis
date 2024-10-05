You can use the built-in `sort` package in Go to sort the slice of integers and the `set` package to remove duplicates. Here is the implementation:

```go
package main

import (
	"fmt"
	"sort"
)

// Return sorted Unique elements in a list
// >>> Unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
// [0, 2, 3, 5, 9, 123]
func Unique(l []int) []int {

	// Create a set to store unique elements
	m := make(map[int]bool)

	// Create a slice to store the unique elements
	var result []int

	// Iterate over the input slice
	for _, v := range l {
		// Check if the element is not present in the set
		if !m[v] {
			// Add the element to the set
			m[v] = true
			// Add the element to the result slice
			result = append(result, v)
		}
	}

	// Sort the result slice
	sort.Ints(result)

	return result
}

func main() {
	fmt.Println(Unique([]int{5, 3, 5, 2, 3, 3, 9, 0, 123}))
}
```

In this code, we create a map `m` to store unique elements. We iterate over the input slice and for each element, we check if it is not present in the map. If it is not present, we add it to the map and the result slice. Finally, we sort the result slice using the `sort.Ints` function and return it. In the `main` function, we call the `Unique` function with a sample input slice and print the result. The output will be `[0, 2, 3, 5, 9, 123]`.