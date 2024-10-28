You can use a filter function to achieve this. Here's a simple implementation in Go:

```go
package main

import (
	"fmt"
	"reflect"
)

func FilterIntegers(values []interface{}) []int {
	var result []int
	for _, value := range values {
		v := reflect.ValueOf(value)
		if v.Kind() == reflect.Int {
			result = append(result, v.Int())
		}
	}
	return result
}

func main() {
	fmt.Println(FilterIntegers([]interface{}{"a", 3.14, 5})) // [5]
	fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", map[string]int{"a": 1}, []int{1, 2}})) // [1 2 3]
}
```

This program uses the `reflect` package to determine the type of each value in the slice. If the value is an integer, it adds it to the result slice. The `reflect.ValueOf` function returns a `Value` object that represents the value, and the `Kind` method returns the type of the value. If the kind is `Int`, the value is an integer, so it is added to the result slice. The `Int` method returns the integer value. The `append` function is used to add the integer to the result slice. The result slice is then returned. In the `main` function, the `FilterIntegers` function is called with two slices of values, and the results are printed. The first call returns `[5]`, and the second call returns `[1 2 3]`.