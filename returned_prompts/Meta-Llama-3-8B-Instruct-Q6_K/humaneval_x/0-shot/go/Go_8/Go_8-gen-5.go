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
Explanation:
This Go program defines a function `SumProduct` that takes a slice of integers as input and returns a tuple consisting of the sum and product of all the integers in the slice. If the input slice is empty, the function returns a tuple with sum as 0 and product as 1.

The `SumProduct` function uses a for loop to iterate over the input slice. Inside the loop, it calculates the sum by adding each number to the current sum, and calculates the product by multiplying each number with the current product.

Finally, the function returns a tuple with the calculated sum and product.

In the `main` function, we test the `SumProduct` function with an empty slice and a slice with some numbers. The output is printed to the console.

The output will be:
```
(0, 1)
(10, 24)
```


Time complexity: O(n), where n is the number of elements in the input slice.
Space complexity: O(1), as we are using a fixed amount of space to store the sum and product.