
if n < 0 {
		return -1
	}

	if n == 0 || n == 1 {
		return 0
	}

	if n == 2 {
		return 1
	}

	a := 0
	b := 0
	c := 1
	res := 0

	for i := 3; i <= n; i++ {
		res = a + b + c
		a = b
		b = c
		c = res
	}

	return res
}

*/

package main

import (
	"fmt"
)

func Fibfib(n int) int {
	if n < 0 {
		return -1
	}
	if n == 0 || n == 1 {
		return 0
	}
	if n == 2 {
		return 1
	}
	a, b, c := 0, 0, 1
	for i := 3; i <= n; i++ {
		a, b, c = b, c, a+b+c
	}
	return c
}

func main() {
	fmt.Println(Fibfib(1)) // 0
	fmt.Println(Fibfib(5)) // 4
	fmt.Println(Fibfib(8)) // 24
}
/*

