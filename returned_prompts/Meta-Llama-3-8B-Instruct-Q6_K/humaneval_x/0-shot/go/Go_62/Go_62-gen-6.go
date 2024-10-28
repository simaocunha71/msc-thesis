```go
package main

import "fmt"

func Derivative(xs []int) []int {
    if len(xs) == 0 {
        return []int{}
    }
    result := make([]int, len(xs)-1)
    for i := 1; i < len(xs); i++ {
        result[i-1] = xs[i] * i
    }
    return result
}

func main() {
    fmt.Println(Derivative([]int{3, 1, 2, 4, 5}))  // [1, 4, 12, 20]
    fmt.Println(Derivative([]int{1, 2, 3}))  // [2, 6]
}
```
The code defines a function `Derivative` that takes a slice of integers representing the coefficients of a polynomial and returns a new slice representing the derivative of that polynomial.

The derivative of a polynomial is calculated by multiplying each term by its exponent and then decrementing the exponent. The `Derivative` function creates a new slice, `result`, to store the derivative coefficients. It then iterates over the input slice, starting from the second term (since the first term is a constant and has no derivative), and multiplies each term by its exponent (which is its position in the slice, minus one) to get the derivative coefficient. The resulting coefficients are stored in the `result` slice, which is then returned.

In the `main` function, the `Derivative` function is called with two different input slices, and the resulting derivative coefficients are printed to the console. The output matches the expected results:

```
[1, 4, 12, 20]
[2, 6]
```



