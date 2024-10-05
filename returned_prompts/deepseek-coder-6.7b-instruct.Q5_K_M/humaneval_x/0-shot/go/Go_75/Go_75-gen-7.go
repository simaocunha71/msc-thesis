
// Write your solution here

}

*/

package main

import (
	"fmt"
	"math"
)

func IsMultiplyPrime(a int) bool {
	if a < 2 {
		return false
	}
	count := 0
	for i := 2; i <= int(math.Sqrt(float64(a))); i++ {
		if a%i == 0 {
			count++
			for a%i == 0 {
				a = a / i
			}
			if a%i == 0 {
				return false
			}
		}
	}
	if a > 1 {
		count++
	}
	return count%2 == 1
}

func main() {
	fmt.Println(IsMultiplyPrime(30))
}
package main

import "fmt"

func IsMultiplyPrime(a int) bool {
	if a < 2 {
		return false
	}
	count := 0
	for i := 2; i*i <= a; i++ {
		for a%i == 0 {
			count++
			a = a / i
		}
	}
	if a > 1 {
		count++
	}
	return count%2 == 1
}

func main() {
	fmt.Println(IsMultiplyPrime(30))
}
package main

import (
	"fmt"
	"math"
)

// IsMultiplyPrime function checks if the given number is a product of 3 prime numbers.
func IsMultiplyPrime(a int) bool {
	if a < 2 {
		return false
	}
	count := 0
	for i := 2; i <= int(math.Sqrt(float64(a))); i++ {
		if a%i == 0 {
			for a%i == 0 {
				a = a / i
			}
			count++
		}
	}
	if a > 1 {
		count++
	}
	return count%2 == 1
}

func main() {
	fmt.Println(IsMultiplyPrime(30