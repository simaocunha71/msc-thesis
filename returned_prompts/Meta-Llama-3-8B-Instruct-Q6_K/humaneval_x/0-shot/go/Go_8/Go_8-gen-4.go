```go
package main

import "fmt"

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
    fmt.Println(SumProduct([]int{})) // (0, 1)
    fmt.Println(SumProduct([]int{1, 2, 3, 4})) // (10, 24)
}
```



Explanation:

1. The `SumProduct` function takes a slice of integers `numbers` as input.
2. It initializes two variables: `sum` set to 0 and `product` set to 1.
3. It then iterates over the input slice using a `for` loop, and for each integer `num` in the slice:
   - It adds `num` to `sum`.
   - It multiplies `num` with `product`.
4. Finally, it returns a tuple (or a slice of length 2 in Go) containing the calculated `sum` and `product`.
5. In the `main` function, we test the `SumProduct` function with an empty slice and a slice with integers {1, 2, 3, 4}, and print the results.