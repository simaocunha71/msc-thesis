
}
*/

import "fmt"

func Fib(n int) int {
	if n <= 1 {
		return n
	}

	prev := 0
	next := 1
	var fib int

	for i := 2; i <= n; i++ {
		fib = prev + next
		prev = next
		next = fib
	}

	return fib
}

func main() {
	fmt.Println(Fib(10)) // 55
	fmt.Println(Fib(1))  // 1
	fmt.Println(Fib(8))  // 21
}
package main

import (
	"fmt"
	"strings"
)

/*
