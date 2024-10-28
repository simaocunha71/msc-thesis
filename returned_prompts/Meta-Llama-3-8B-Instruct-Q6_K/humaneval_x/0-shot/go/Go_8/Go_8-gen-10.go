```go
package main

import (
    "fmt"
)

func SumProduct(numbers []int) [2]int {
    var sum int
    var product int = 1
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


The function `SumProduct` takes a slice of integers as an input. It initializes two variables `sum` and `product` to 0 and 1 respectively. It then iterates over each number in the input slice and adds it to `sum` and multiplies it with `product`. Finally, it returns a tuple (slice of length 2) consisting of the `sum` and `product`. The `main` function demonstrates the usage of the `SumProduct` function by calling it with an empty slice and a slice with numbers 1, 2, 3, 4. The output is printed to the console.