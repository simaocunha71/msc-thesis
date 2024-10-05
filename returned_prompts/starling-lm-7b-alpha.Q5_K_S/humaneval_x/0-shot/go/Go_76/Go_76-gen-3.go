
```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println(IsSimplePower(1, 4))
	fmt.Println(IsSimplePower(2, 2))
	fmt.Println(IsSimplePower(8, 2))
	fmt.Println(IsSimplePower(3, 2))
	fmt.Println(IsSimplePower(3, 1))
	fmt.Println(IsSimplePower(5, 3))
}

func IsSimplePower(x int,n int) bool {
	for i := 0; i < 32; i++ {
		if n == int(pow(x, float64(i))) {
			return true
		}
	}
	return false
}

func pow(base, exponent float64) float64 {
	if exponent == 0 {
		return 1
	}

	if exponent % 2 == 0 {
		return pow(base*base, exponent/2)
	} else {
		return pow(base*base, exponent/2)*base
	}
}
```

Explanation:

The function IsSimplePower(x, n) takes two integer parameters: x and n. It checks whether x is a simple power of n.

The function pow(base, exponent) is a helper function that calculates the power of a number. It uses the exponentiation by squaring algorithm to optimize the calculation. The function returns the result of base raised to the power of exponent.

In the main function, we test the IsSimplePower function with several test cases to verify its correctness.

The IsSimplePower function iterates through the powers of n (from 0 to 31) using a for loop. Inside the loop, it checks if n is equal to the result of x raised to the power of i. If it is, the function returns true, indicating that x is a simple power of n. If none of the powers of n match x, the function returns false, indicating that x is not a simple power of n.

The pow function calculates the power of a number using the exponentiation by squaring algorithm. It first checks