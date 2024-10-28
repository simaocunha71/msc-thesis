Here is a Go solution that filters a list of values and returns a new list containing only the integers:
```go
package main

import (
	"fmt"
	"reflect"
)

func FilterIntegers(values []interface{}) []int {
	var result []int
	for _, value := range values {
		rv := reflect.ValueOf(value)
		if rv.Kind() == reflect.Int {
			result = append(result, rv.Int())
		}
	}
	return result
}

func main() {
	fmt.Println(FilterIntegers([]interface{}{'a', 3.14, 5})) // [5]
	fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", map[string]int{"a": 1}, []int{1, 2, 3}})) // [1, 2, 3]
}
```
In the `FilterIntegers` function, we iterate over the input values using a range loop. For each value, we use the `reflect` package to inspect its type and kind. If the value is an integer (i.e., its kind is `reflect.Int`), we append it to the result slice.

In the `main` function, we test the `FilterIntegers` function with two examples. The first example filters a list containing a string, a float, and an integer, and returns a list containing only the integer. The second example filters a list containing integers, a string, a map, and a slice, and returns a list containing only the integers.