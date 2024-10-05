```go
package main

import (
	"fmt"
	"math/big"
)

func F(n int) []int {
	result := make([]int, n)
	for i := 1; i <= n; i++ {
		if i%2 == 0 {
			factorial := big.NewInt(1)
			for j := 2; j <= i; j++ {
				factorial.Mul(factorial, big.NewInt(int64(j)))
			}
			result[i-1] = int(factorial.Int64())
		} else {
			sum := 0
			for j := 1; j <= i; j++ {
				sum += j
			}
			result[i-1] = sum
		}
	}
	return result
}

func main() {
	fmt.Println(F(5)) // [1, 2, 6, 24, 15]
}
```


Explanation:

1. We create a slice `result` of size `n` to store the result.
2. We iterate over the range from 1 to `n` using a for loop.
3. For each `i`, we check if it's even by using the modulus operator `%`. If it's even, we calculate the factorial of `i` using a `big.Int` variable `factorial`. We initialize `factorial` to 1 and then multiply it by each number from 2 to `i` using the `Mul` method. Finally, we convert the result to an `int` and store it in the `result` slice.
4. If `i` is odd, we calculate the sum of numbers from 1 to `i` using a variable `sum`. We iterate over the range from 1 to `i` and add each number to `sum`. Finally, we store the result in the `result` slice.
5. We return the `result` slice.

The `big` package is used to handle large integers, as the factorial of a large number can exceed the maximum value of an `int`. The `math/big` package provides support for arbitrary-precision arithmetic, which is useful for this problem.