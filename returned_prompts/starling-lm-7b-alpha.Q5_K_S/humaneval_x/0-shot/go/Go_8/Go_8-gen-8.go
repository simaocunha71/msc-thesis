
```go
func SumProduct(numbers []int) [2]int {
    sum, product := 0, 1
    for _, number := range numbers {
        sum += number
        product *= number
    }
    return [2]int{sum, product}
}
```

In this solution, we use two variables, `sum` and `product` to store the sum and the product of all the integers in the list respectively. We initialize `sum` to 0 and `product` to 1.

We iterate over each number in the list using a for loop. For each number, we add it to the `sum` and multiply it with the `product`. After iterating through all the numbers, we return a tuple consisting of the `sum` and the `product`.

For example, when we call `SumProduct([])`, the function will return `(0, 1)` because there are no numbers in the list and the sum and product of an empty list are 0 and 1 respectively.

When we call `SumProduct([1, 2, 3, 4])`, the function will return `(10, 24)` because the sum of all the numbers in the list is 10 and the product of all the numbers in the list is 24.

The time complexity of this solution is O(n) because we iterate over each number in the list exactly once. The space complexity is also O(1) because we only use a constant amount of extra space to store the `sum` and the `product`.

This solution is efficient and has a low space complexity, making it a good choice for calculating the sum and product of a list of integers.

Here's an example of how you can use this function in your program:

```go
package main

import "fmt"

func main() {
    fmt.Println(SumProduct([]int{})) // (0, 1)
    fmt.Println(SumProduct([]int{1, 2, 3, 4})) // (10, 24)
}
```

This will output:
```
(0, 1)
(10, 24)
```

You can try running