You can solve this problem in Go by using the built-in functions len() and range to iterate over the numbers, and the built-in functions sum() and prod() to calculate the sum and product of the numbers. Here is the code:

```go
package main

import (
    "fmt"
    "math"
)

func SumProduct(numbers []int) [2]int {
    sum := 0
    prod := 1
    for _, num := range numbers {
        sum += num
        prod *= num
    }
    if prod == 0 {
        prod = 1
    }
    return [2]int{sum, prod}
}

func main() {
    fmt.Println(SumProduct([]int{}))    // Output: [0 1]
    fmt.Println(SumProduct([]int{1, 2, 3, 4}))    // Output: [10 24]
}
```

The code defines a function SumProduct() that takes a slice of integers as input and returns a tuple consisting of the sum and product of the integers in the slice. The function uses a loop to iterate over the numbers in the slice, and the built-in functions sum() and prod() to calculate the sum and product of the numbers. The function also checks if the product is zero and sets it to one if it is. The function is then called in the main() function to test the code.