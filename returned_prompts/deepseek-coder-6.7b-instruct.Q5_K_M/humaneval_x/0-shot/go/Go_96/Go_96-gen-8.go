
// check if n is less than 2, if yes then return empty array
if n < 2 {
return []
}

// declare an empty array to store prime numbers
primes := []int{}

// iterate through numbers 2 to n
for i := 2; i < n; i++ {

// check if current number is prime
if isPrime(i) {

// if yes then add it to the primes array
primes = append(primes, i)
}
}

// return the primes array
return primes
}

// helper function to check if a number is prime
func isPrime(n int) bool {

// iterate through numbers 2 to sqrt(n)
for i := 2; i*i <= n; i++ {

// if n is divisible by any number in this range then it's not a prime
if n%i == 0 {
return false
}
}

// if none of the numbers in the range divide n then n is a prime
return true
}

*/

package main

import (
	"fmt"
	"math"
)

func CountUpTo(n int) []int {
	if n < 2 {
		return []int{}
	}
	primes := []int{}
	for i := 2; i < n; i++ {
		if isPrime(i) {
			primes = append(primes, i)
		}
	}
	return primes
}

func isPrime(n int) bool {
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(CountUpTo(5))
	fmt.Println(CountUpTo(11))
	fmt.Println(CountUpTo(0))
	fmt.Println(CountUpTo(20))
	fmt.Println(CountUpTo(1))
	fmt.Println(CountUpTo(18))
}
package main

import (
	"