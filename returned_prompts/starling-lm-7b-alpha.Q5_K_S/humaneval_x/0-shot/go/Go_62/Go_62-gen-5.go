
Here's a working solution in Go:

```go
package main

import "fmt"

func Derivative(xs []int) []int {
    l := len(xs)
    res := make([]int, l-1)
    for i := 1; i < l; i++ {
        res[i-1] = i * xs[i]
    }
    return res
}

func main() {
    fmt.Println(Derivative([]int{3, 1, 2, 4, 5}))
    fmt.Println(Derivative([]int{1, 2, 3}))
}
```

Explanation:

The derivative of a polynomial is computed by taking the derivative of each term in the polynomial. The derivative of a term is calculated by multiplying the coefficient of the term by the power of the term and incrementing the power by one.

In the given solution, a function `Derivative` is defined that takes a slice `xs` of integers representing the coefficients of a polynomial. It initializes an empty slice `res` of the same length as `xs` to store the derivative of the polynomial.

Next, a for loop is used to iterate over the indices of `xs` starting from index 1 (since the derivative of the constant term is always zero). For each index `i`, the derivative of the corresponding term is calculated by multiplying the coefficient `xs[i]` by `i` (the power of the term) and appending the result to the `res` slice at index `i-1`. This is done to maintain the correct order of the derivative terms.

Finally, the `res` slice is returned as the derivative of the polynomial.

In the `main` function, the `Derivative` function is called with two example inputs and the results are printed using `fmt.Println`.

The output of the provided test cases are:

```
[1 4 12 20]
[2 6]
```

These are the correct derivatives of the input polynomials `[3, 1, 2, 4, 5]` and `[1, 2, 3]`, respectively.

```go
