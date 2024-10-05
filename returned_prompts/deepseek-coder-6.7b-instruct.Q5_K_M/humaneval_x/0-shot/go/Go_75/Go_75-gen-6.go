
}

*/

import "fmt"

func IsMultiplyPrime(a int) bool {
	count := 0
	for i := 2; i*i <= a; i++ {
		if a%i == 0 {
			for a%i == 0 {
				a = a / i
				count++
			}
			if count > 1 {
				return false
			}
		}
	}
	if a != 1 && count == 1 {
		return false
	}
	if count == 1 {
		return true
	}
	return false
}

func main() {
	fmt.Println(IsMultiplyPrime(30))
}
package main

import (
	"fmt"
	"math"
)

/*
