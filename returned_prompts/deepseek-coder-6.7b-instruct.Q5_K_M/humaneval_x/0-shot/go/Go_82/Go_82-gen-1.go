
// first, we need to define a helper function to check if a number is prime.
// a number is prime if it has no divisors other than 1 and itself
func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i * i <= n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}

// then we can use this helper function to check if the length of the string is prime
func PrimeLength(s string) bool {
    return isPrime(len(s))
}

*/

package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
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

func PrimeLength(s string) bool {
	return isPrime(len(s))
}

func main() {
	fmt.Println(PrimeLength("Hello"))    // == true
	fmt.Println(PrimeLength("abcdcba"))  // == true
	fmt.Println(PrimeLength("kittens"))  // == true
	fmt.Println(PrimeLength("orange"))   // == false
}
package main

import "fmt"

func main() {
	a := 10
	b := 20
	c := 30
	d := 40

	if a < b && c > b {
		fmt.Println("And Operator: Both conditions are true")
	}

	if a < b || c > d {
		fmt.Println("Or Operator: At least one condition is true")
	}

	if !(a == b) {
		fmt.Println("Not Operator: Condition is false")
	}

}

/*
And Operator: Both conditions are true
Or Operator: At least one condition is true
Not Operator