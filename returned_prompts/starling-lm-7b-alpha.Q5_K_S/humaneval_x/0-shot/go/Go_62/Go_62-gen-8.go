
```go
package main

import "fmt"

func Derivative(xs []int) []int {
	n := len(xs)
	result := make([]int, n-1)
	for i := 1; i < n; i++ {
		result[i-1] = xs[i] * i
	}
	return result
}

func main() {
	xs := []int{3, 1, 2, 4, 5}
	fmt.Println(Derivative(xs))
	
	xs = []int{1, 2, 3}
	fmt.Println(Derivative(xs))
}
```

Explanation:

In this exercise, you're asked to write a function to compute the derivative of a polynomial, represented as a slice of integers `[]int`. The derivative of a polynomial `P(x) = a0 + a1 * x + a2 * x^2 + ... + an * x^n` is a new polynomial `Q(x) = a1 + a2 * 2 * x + ... + an * (n + 1) * x^(n-1)`.

The function `Derivative` takes a slice of integers `xs` as an argument and returns a new slice of integers. The length of the returned slice is one less than the length of the input slice, as the first coefficient (`a0`) is zero in the derivative of a polynomial.

The function uses a for loop to iterate over the input slice from the second element (`i = 1`) to the last element (`i < n`). For each element, it computes the derivative of that element by multiplying it by the index `i` and stores the result in the corresponding position in the result slice (`result[i-1] = xs[i] * i`).

Finally, the function returns the result slice, which represents the derivative of the input polynomial.

In the `main` function, the `Derivative` function is called with two different input slices (`xs = []int{3, 1, 2, 4, 5}` and `xs = []int{1, 2, 3}`).