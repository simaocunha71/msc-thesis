
// base cases
if n <= 0 {
    return 0
}
if n == 1 {
    return 1
}

// recursive case
return Fib(n-1) + Fib(n-2)
}
*/

func Fib(n int) int {
	if n <= 0 {
		return 0
	}
	if n == 1 {
		return 1
	}

	return Fib(n-1) + Fib(n-2)
}

func main() {
	fmt.Println(Fib(10))
	fmt.Println(Fib(1))
	fmt.Println(Fib(8))
}
package main

import (
	"fmt"
)

/*
