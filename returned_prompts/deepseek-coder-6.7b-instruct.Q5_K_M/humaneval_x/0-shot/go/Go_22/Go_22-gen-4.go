    var result []int

    for _, value := range values {
        if val, ok := value.(int); ok {
            result = append(result, val)
        }
    }

    return result
}

// Test
func main() {
    fmt.Println(FilterIntegers([]interface{}{'a', 3.14, 5})) // [5]
    fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", map[string]int{}, []int{}})) // [1, 2, 3]
}
```

This is a simple solution to the problem in Go. This function `FilterIntegers` takes a slice of empty interfaces as an argument, then iterates over the slice and checks if each value is an integer. If it is, it appends it to the `result` slice which is returned at the end.

This works because the `value.(int)` syntax is a type assertion. It attempts to convert the `value` to an `int`. If it succeeds, `ok` is `true` and `val` is the integer value. If it fails, `ok` is `false` and `val` is the zero value of an `int` (which is `0`).

The test cases show that this function works as expected.

Please note that this function will not work for float values that are equal to integer values, as float values are not integers. If you want to include such values, you need to modify the function to handle float values as well.
*/
package main

import (
	"fmt"
)

// Filter given list of any values only for integers
func FilterIntegers(values []interface{}) []int {
	var result []int

	for _, value := range values {
		if val, ok := value.(int); ok {
			result = append(result, val)
		}
	}

	return result
}

func main() {
	fmt.Println(FilterIntegers([]interface{}{'a', 3.14, 5}))                                 // [5]
	fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc