
// Base case: 0th and 1st Fibonacci numbers are the same.
if n == 0 || n == 1 {
    return n
}

// Recursive case: the nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers.
return Fib(n-1) + Fib(n-2)
}

*/

package main

import (
	"fmt"
)

func Fib(n int) int {
	if n == 0 || n == 1 {
		return n
	}
	return Fib(n-1) + Fib(n-2)
}

func main() {
	fmt.Println(Fib(10))
	fmt.Println(Fib(1))
	fmt.Println(Fib(8))
}
/*

