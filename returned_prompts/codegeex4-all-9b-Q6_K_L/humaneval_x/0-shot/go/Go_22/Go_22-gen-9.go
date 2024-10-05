You can use the built-in `strconv` package in Go to check if a value is an integer. Here's how you can modify the `FilterIntegers` function to filter out only the integers from the given list:

```go
package main

import (
	"fmt"
	"strconv"
)

func FilterIntegers(values []interface{}) []int {
	var integers []int
	for _, value := range values {
		// Check if value can be converted to an integer
		if _, ok := value.(int); ok {
			integers = append(integers, value.(int))
		}
	}
	return integers
}

func main() {
	values := []interface{}{"a", 3.14, 5, 1, 2, 3, "abc", map[string]string{}, []string{}}
	integers := FilterIntegers(values)
	fmt.Println(integers) // Output: [5 1 2 3]
}
```

In this modified function, we use a type assertion to check if each value in the list can be converted to an integer. If it can, we append it to the `integers` slice. Finally, we return the `integers` slice, which contains only the integers from the input list.