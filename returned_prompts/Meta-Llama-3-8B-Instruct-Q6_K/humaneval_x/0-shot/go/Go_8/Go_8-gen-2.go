```go
package main

import (
    "fmt"
)

func SumProduct(numbers []int) [2]int {
    sum := 0
    product := 1
    for _, num := range numbers {
        sum += num
        product *= num
    }
    return [2]int{sum, product}
}

func main() {
    fmt.Println(SumProduct([]int{}))  // (0, 1)
    fmt.Println(SumProduct([]int{1, 2, 3, 4}))  // (10, 24)
}
```



The provided Go function `SumProduct` calculates the sum and product of all integers in a given list. It initializes two variables, `sum` and `product`, to 0 and 1, respectively. Then, it iterates over the list using a range-based for loop, adding each number to `sum` and multiplying each number to `product`. Finally, it returns a tuple (or a slice of two integers in Go) containing the calculated `sum` and `product`.

The `main` function demonstrates the usage of the `SumProduct` function with two test cases: an empty list `[]int{}` and a list with numbers `[1, 2, 3, 4]`. The expected output is `(0, 1)` for the empty list and `(10, 24)` for the list with numbers. The program prints these results using the `fmt.Println` function.