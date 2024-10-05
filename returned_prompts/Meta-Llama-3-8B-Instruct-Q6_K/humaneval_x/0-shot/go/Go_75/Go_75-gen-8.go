```go
package main

import (
	"fmt"
	"math"
)

func IsPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func IsMultiplyPrime(a int) bool {
	for i := 2; i <= a; i++ {
		if IsPrime(i) {
			for j := i; j <= a; j++ {
				if IsPrime(j) {
					for k := j; k <= a; k++ {
						if IsPrime(k) && i*j*k == a {
							return true
						}
					}
				}
			}
		}
	}
	return false
}

func main() {
	fmt.Println(IsMultiplyPrime(30)) // Output: true
}
```



Explanation:

The task is to write a function `IsMultiplyPrime` that takes an integer `a` as an input and returns `true` if `a` is the multiplication of three prime numbers and `false` otherwise.

The function `IsMultiplyPrime` iterates over all numbers from 2 to `a`. For each number `i`, it checks if `i` is prime using the `IsPrime` function. If `i` is prime, it then iterates over all numbers from `i` to `a` and checks if `j` is prime. If `j` is prime, it then iterates over all numbers from `j` to `a` and checks if `k` is prime. If `k` is prime and `i*j*k` equals `a`, the function returns `true`.

The `IsPrime` function checks if a number `n` is prime by iterating from 2 to the square root of `n` and checking if `n` is divisible by any of these numbers. If `n` is divisible, it is not prime, and the function returns `false`. Otherwise, it returns `true`.

In the `main` function, we test the `IsMultiplyPrime` function with the input `30`, which is the multiplication of 2, 3, and 5, and it returns `true` as expected.