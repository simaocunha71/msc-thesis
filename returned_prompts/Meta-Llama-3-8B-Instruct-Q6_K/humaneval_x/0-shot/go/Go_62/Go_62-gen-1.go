```go
package main

import (
	"fmt"
)

func Derivative(xs []int) []int {
	if len(xs) == 0 {
		return nil
	}
	result := make([]int, len(xs)-1)
	for i := 0; i < len(result); i++ {
		result[i] = xs[i+1] * (i + 1)
	}
	return result
}

func main() {
	fmt.Println(Derivative([]int{3, 1, 2, 4, 5})) // Output: [1, 4, 12, 20]
	fmt.Println(Derivative([]int{1, 2, 3})) // Output: [2, 6]
}
```



Explanation:
The derivative of a polynomial is calculated by taking the derivative of each term and multiplying it by the power of the term. The derivative of a term `a*x^n` is `n*a*x^(n-1)`. 

In this Go function, we iterate through the input array `xs` and calculate the derivative of each term. We start from the second term (index 1) since the derivative of the first term is 0. For each term, we multiply the coefficient by its power and return the result in a new array. The length of the result array is one less than the input array since the derivative of a constant is 0. 

In the main function, we test the `Derivative` function with two examples and print the results. The output is as expected: `[1, 4, 12, 20]` for the input `[3, 1, 2, 4, 5]` and `[2, 6]` for the input `[1, 2, 3]`. 