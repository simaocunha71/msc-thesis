Here is the implementation in Go:

```go
package main

import (
	"fmt"
	"reflect"
)

func FilterIntegers(values []interface{}) []int {
	var result []int
	for _, v := range values {
		rv := reflect.ValueOf(v)
		if rv.Kind() == reflect.Int {
			result = append(result, rv.Int())
		}
	}
	return result
}

func main() {
	fmt.Println(FilterIntegers([]interface{}{"a", 3.14, 5})) // [5]
	fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", map[string]int{"a": 1}, []int{1, 2, 3}})) // [1, 2, 3]
}
```

In this code, we use the `reflect` package to check the type of each value in the slice. If the value is an integer, we append it to the `result` slice. The `reflect.ValueOf(v).Kind()` function returns the type of the value, which can be used to check if it's an integer. The `reflect.ValueOf(v).Int()` function returns the value as an integer. If the value is not an integer, we ignore it and move on to the next value. The `FilterIntegers` function returns the `result` slice, which contains all the integers from the original slice.