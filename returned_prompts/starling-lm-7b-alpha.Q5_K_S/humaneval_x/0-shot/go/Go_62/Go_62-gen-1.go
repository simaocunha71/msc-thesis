To calculate the derivative of a polynomial, we can use the following formula:

For xs[0] + xs[1] * x + xs[2] * x^2 + ....

Derivative = [xs[1] * 1 + xs[2] * 2 * x + xs[3] * 3 * x^2 + ...]

This means that the derivative of the first term in the polynomial is the second term, the derivative of the second term is twice the third term, and so on.

To implement this in Go, we can use a simple loop to calculate the derivative and return it as a slice of integers.

Here's a sample Go implementation:

```go
package main

import "fmt"

func Derivative(xs []int) []int {
    result := make([]int, len(xs)-1)
    for i := range result {
        result[i] = xs[i+1] * (i + 1)
    }
    return result
}

func main() {
    fmt.Println(Derivative([]int{3, 1, 2, 4, 5})) // [1, 4, 12, 20]
    fmt.Println(Derivative([]int{1, 2, 3}))       // [2, 6]
}
```

In this implementation, we first create a slice called `result` to store the derivative values. We initialize it with a length of `len(xs)-1`, as the derivative of a polynomial of degree `n` will have `n-1` terms.

Then, we use a `for` loop to iterate over the `result` slice. For each index `i`, we calculate the derivative term by multiplying `xs[i+1]` (the next coefficient in the original polynomial) with `(i + 1)` (the power of `x` for the current term in the derivative). We store this value in the `result` slice at index `i`.

Finally, we return the `result` slice, which contains the derivative of the original polynomial.

You can test the implementation by running the provided sample code, which prints the derivatives of two example polynomials