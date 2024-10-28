
// Your code here

}

*/

func IsMultiplyPrime(a int) bool {
	if a == 1 {
		return false
	}
	count := 0
	for i := 2; i*i <= a; i++ {
		if a%i == 0 {
			for a%i == 0 {
				a = a / i
				count++
			}
			if isPrime(i) == false || count > 3 {
				return false
			}
		}
	}
	if a != 1 && isPrime(a) {
		count++
	}
	return count == 3
}

func isPrime(n int) bool {
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(IsMultiplyPrime(30)) // true
	fmt.Println(IsMultiplyPrime(10)) // false
	fmt.Println(IsMultiplyPrime(36)) // true
	fmt.Println(IsMultiplyPrime(14)) // false
	fmt.Println(IsMultiplyPrime(1))  // false
}

/*
Test Result:
true
false
true
false
false
*/
package main

import (
	"fmt"
	"math"
)

/*
