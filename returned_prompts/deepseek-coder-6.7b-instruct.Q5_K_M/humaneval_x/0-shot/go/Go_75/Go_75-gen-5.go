
	primes := []int{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}

	count := 0

	for _, prime := range primes {
		if a % prime == 0 {
			count += 1
		}
	}

	if count >= 3 {
		return true
	}

	return false

}

// Implement the function IsMultiplyPrime
// IsMultiplyPrime(30) should return true
// IsMultiplyPrime(31) should return false
func main() {

	a := 30
	b := 31

	fmt.Println(IsMultiplyPrime(a)) // should return true
	fmt.Println(IsMultiplyPrime(b)) // should return false

}



*/
package main

import "fmt"

func IsMultiplyPrime(a int) bool {

	primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

	count := 0

	for _, prime := range primes {
		if a%prime == 0 {
			count += 1
		}
	}

	if count >= 3 {
		return true
	}

	return false

}

func main() {

	a := 30
	b := 31

	fmt.Println(IsMultiplyPrime(a)) // should return true
	fmt.Println(IsMultiplyPrime(b)) // should return false

}

// IsMultiplyPrime