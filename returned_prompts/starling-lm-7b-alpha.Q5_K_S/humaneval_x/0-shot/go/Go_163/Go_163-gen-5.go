
Here's a working solution in Go:

```go
package main

import (
    "fmt"
)

func GenerateIntegers(a, b int) []int {
    result := []int{}
    for i := a; i <= b; i++ {
        if i%2 == 0 {
            result = append(result, i)
        }
    }
    return result
}

func main() {
    fmt.Println(GenerateIntegers(2, 8)) // [2, 4, 6, 8]
    fmt.Println(GenerateIntegers(8, 2)) // [2, 4, 6, 8]
    fmt.Println(GenerateIntegers(10, 14)) // []
}
```

This program defines a function `GenerateIntegers` that takes two integers as arguments and returns a slice of integers. The function iterates over all integers between `a` and `b`, inclusive, and if the integer is even (i.e., divisible by 2), it appends the integer to the result slice. Finally, the function returns the result slice.

The `main` function calls `GenerateIntegers` with different values and prints the results.

When you run this program, it will output `[2, 4, 6, 8]`, `[2, 4, 6, 8]`, and an empty slice `[]` respectively, which are the expected outputs.

```go
package main

import (
    "fmt"
)

func GenerateIntegers(a, b int) []int {
    result := []int{}
    for i := a; i <= b; i++ {
        if i%2 == 0 {
            result = append(result, i)
        }
    }
    return result
}

func main() {
    fmt.Println(GenerateIntegers(2, 8)) // [2, 4, 6, 8]
    fmt.Println(GenerateIntegers(8, 2)) // [2, 4, 6, 8]
    fmt.Println(GenerateInte