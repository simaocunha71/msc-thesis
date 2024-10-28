To filter a given list of values only for integers, you can define a function called FilterIntegers that takes in a slice of interface type called values. Inside the function, initialize an empty slice of integer type called integers. Then, iterate through each element of the values slice using a for loop. Within the loop, use a type assertion to check if the current element is of type int. If it is, append it to the integers slice using the append function. Here's an example implementation:

```go
func FilterIntegers(values []interface{}) []int {
    integers := []int{}
    for _, value := range values {
        if _, ok := value.(int); ok {
            integers = append(integers, value.(int))
        }
    }
    return integers
}
```

To test the function, you can use the `fmt.Println` function to print the result of calling the `FilterIntegers` function with different input slices. For example:

```go
fmt.Println(FilterIntegers([]interface{}{"a", 3.14, 5}))
fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", map[string]interface{}{}, []interface{}{}}))
```

The output will be:
```
[5]
[1, 2, 3]
```

This way, the function will filter out all non-integer values from the input slice and return a new slice containing only the integer values.

Hope this helps!

```go
package main

import "fmt"

func main() {
    fmt.Println(FilterIntegers([]interface{}{"a", 3.14, 5}))
    fmt.Println(FilterIntegers([]interface{}{1, 2, 3, "abc", map[string]interface{}{}, []interface{}{}}))
}

func FilterIntegers(values []interface{}) []int {
    integers := []int{}
    for _, value := range values {
        if _, ok := value.(int); ok {
            integers = append(integers, value.(int))
        }
    }
    return inte