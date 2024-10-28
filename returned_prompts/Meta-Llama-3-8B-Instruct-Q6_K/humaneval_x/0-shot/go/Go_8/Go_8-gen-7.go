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



In the code above, we define a function `SumProduct` that takes a slice of integers as an input. The function initializes two variables `sum` and `product` to 0 and 1 respectively. It then iterates over the input slice using a for loop, adding each number to `sum` and multiplying each number with `product`. Finally, it returns a tuple of `sum` and `product`.

In the `main` function, we test the `SumProduct` function with an empty slice and a slice containing numbers 1, 2, 3, and 4. The output of the program is `(0, 1)` and `(10, 24)` respectively, which is the expected result.