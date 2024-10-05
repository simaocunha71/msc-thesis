
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
    fmt.Println(SumProduct([]int{}))         // Output: [0 1]
    fmt.Println(SumProduct([]int{1, 2, 3, 4})) // Output: [10 24]
}
```

In the code above, we define a function `SumProduct` which takes a slice of integers as argument. It initializes two variables `sum` and `product` to 0 and 1 respectively. Then it iterates over the numbers in the slice, adding each number to `sum` and multiplying `product` by the number. Finally, it returns a 2-element array containing `sum` and `product`.

The `main` function tests `SumProduct` with an empty slice and a slice containing the numbers 1 to 4.

This solution has a time complexity of O(n), where n is the number of elements in the input slice.

It also has a space complexity of O(1), because it uses a constant amount of space to store `sum` and `product`, regardless of the size of the input.

It meets the problem requirements.
"""

# Tests

assert(SumProduct([]) == (0, 1))
assert(SumProduct([1, 2, 3, 4]) == (10, 24))
assert(SumProduct([5, 6, 7, 8]) == (26, 1680))
assert(SumProduct([9, 10, 11, 12]) == (42, 479001600))
assert(SumProduct([13, 14, 15, 16]) == (60, 389792607974121664))

print("All tests passed.")
```

This Python program tests