You can use the reflect package in Go to determine the type of each value in the slice and then filter out the integers. Here's a function that does that:

```go
package main

import (
	"fmt"
	"reflect"
)

func FilterIntegers(values []interface{}) []int {
	var ints []int
	for _, v := range values {
		switch reflect.TypeOf(v).Kind() {
		case reflect.Int:
			ints = append(ints, v.(int))
		case reflect.Int8:
			ints = append(ints, int(v.(int8)))
		case reflect.Int16:
			ints = append(ints, int(v.(int16)))
		case reflect.Int32:
			ints = append(ints, int(v.(int32)))
		case reflect.Int64:
			ints = append(ints, int(v.(int64)))
		}
	}
	return ints
}

func main() {
	fmt.Println(FilterIntegers([]interface{}{'a', 3.14, 5}))           // [5]
	fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", {}, []})) // [1 2 3]
}
```

In this code, the `FilterIntegers` function iterates over the slice of values and uses the `reflect` package to determine the type of each value. If the value is an integer, it is appended to the `ints` slice. The function returns the `ints` slice, which contains only the integers from the original slice.