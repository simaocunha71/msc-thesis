Here is a simple and efficient solution using a filter function and the `reflect` package in Go. This function will iterate over the slice of interfaces and check if the value is an integer. If it is, it will add it to the result slice.

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
	fmt.Println(FilterIntegers([]interface{}{'a', 3.14, 5})) // [5]
	fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", {}, []})) // [1, 2, 3]
}
```

This solution works by using the `reflect` package to determine the type of each value in the slice. If the type is an integer, it adds it to the result slice. This way, you can easily filter a slice of interfaces for integers.

Please note that this solution considers only `int` types, if you want to consider other integer types like `int8`, `int16`, `int32`, `int64` you need to add more conditions. 

Also, this solution does not handle the case where the value is a complex number or a float that is not an integer. If you need to handle these cases, you would need to add more conditions. 

It's worth noting that this solution is not the most efficient way to filter a slice of interfaces in Go, especially for large slices. This is because the `reflect` package can be slow for large amounts of data. In such cases, you might want to consider using a different data structure, such as a map, or using a more efficient filtering algorithm. 