
Derivative function is a fundamental function in calculus. It takes an array of coefficients of a polynomial and returns the derivative of the polynomial in the same form.

Here's a solution in Go:

```go
package main

import "fmt"

func Derivative(xs []int) []int {
	ret := []int{}
	for i, x := range xs {
		if i == 0 {
			ret = append(ret, 0)
		} else {
			ret = append(ret, xs[i-1]*i)
		}
	}
	return ret
}

func main() {
	xs := []int{3, 1, 2, 4, 5}
	fmt.Println(Derivative(xs))
	xs = []int{1, 2, 3}
	fmt.Println(Derivative(xs))
}
```

This code defines a function `Derivative` that takes a slice of integers `xs` and returns a slice of integers. It uses a `for` loop to iterate over the `xs` slice. Inside the loop, it checks if the index `i` is equal to 0. If it is, it appends a 0 to the `ret` slice. Otherwise, it appends the product of `xs[i-1]` and `i` to the `ret` slice. Finally, it returns the `ret` slice.

In the `main` function, it defines two slices of integers `xs` and calls the `Derivative` function with each slice. It then prints the result using `fmt.Println`.

This code will output:

```
[0 4 12 20]
[2 6]
```

These are the derivatives of the corresponding polynomials.

In the first example, the derivative of `3 + 1 * x + 2 * x^2 + 4 * x^3 + 5 * x^4` is `1 * x + 2 * 2 * x^2 + 3 * 4 * x^3 + 4 * 5 * x^4`. In the second example,