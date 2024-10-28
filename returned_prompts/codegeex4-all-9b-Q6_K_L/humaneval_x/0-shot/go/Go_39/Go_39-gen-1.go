package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func fib(n int) int {
	if n <= 1 {
		return n
	}
	return fib(n-1) + fib(n-2)
}

func primeFib(n int) int {
	count := 0
	i := 2
	for {
		if isPrime(fib(i)) {
			count++
		}
		if count == n {
			return fib(i)
		}
		i++
	}
}

func main() {
	fmt.Println(primeFib(1)) // 2
	fmt.Println(primeFib(2)) // 3
	fmt.Println(primeFib(3)) // 5
	fmt.Println(primeFib(4)) // 13
	fmt.Println(primeFib(5)) // 89
}

B:
package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func fib(n int) int {
	if n <= 1 {
		return n
	}
	return fib(n-1) + fib(n-2)
}

func primeFib(n int) int {
	count := 0
	i := 2
	for {
		if isPrime(fib(i)) {
			count++
		}
		if count == n {
			return fib(i)
		}
		i++
	}
}

func main() {
	fmt.Println(primeFib(1)) // 2
	fmt.Println(primeFib(2)) // 3
	fmt.Println(primeFib(3)) // 5
	fmt.Println(primeFib(4)) // 13
	fmt.Println(primeFib(5)) //