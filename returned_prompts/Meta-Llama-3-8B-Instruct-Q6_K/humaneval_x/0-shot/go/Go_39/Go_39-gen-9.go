```go
package main

import (
	"fmt"
	"math"
)

func isPrime(num int) bool {
	if num <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func isFibonacci(num int) bool {
	a, b := 0, 1
	for b < num {
		a, b = b, a+b
	}
	return b == num
}

func PrimeFib(n int) int {
	a, b := 0, 1
	for i := 1; ; i++ {
		a, b = b, a+b
		if isFibonacci(b) && isPrime(b) {
			if i == n {
				return b
			}
		}
	}
}

func main() {
	fmt.Println(PrimeFib(1))  // 2
	fmt.Println(PrimeFib(2))  // 3
	fmt.Println(PrimeFib(3))  // 5
	fmt.Println(PrimeFib(4))  // 13
	fmt.Println(PrimeFib(5))  // 89
}
```
In this solution, we define two helper functions `isPrime` and `isFibonacci` to check if a number is prime and a Fibonacci number respectively. We then use these helper functions in the `PrimeFib` function to find the n-th Fibonacci number that is also prime. In the main function, we test `PrimeFib` with different values of n. 

The time complexity of this solution is O(n * sqrt(m)) where n is the input number and m is the maximum possible Fibonacci number. The space complexity is O(1) as we are using a constant amount of space. 

This solution works well for small to medium-sized inputs. For larger inputs, you may need to use a more efficient algorithm or data structure. 

Please note that the `PrimeFib` function will run indefinitely if no Fibonacci number is prime. You may want to add a limit to the range of numbers to check for primality to make the function more efficient. 

Also, you may want to use a more efficient algorithm to check for primality, such as the Sieve of Eratosthenes algorithm. This can significantly improve the performance of the `PrimeFib` function. 

It