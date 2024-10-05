    factors := []int{}
    for i := 2; i <= n; i++ {
        if n%i == 0 {
            factors = append(factors, i)
            n = n / i
            i--
        }
        if n == 1 {
            break
        }
    }
    return factors
}

func main() {
    fmt.Println(Factorize(8))  // [2 2 2]
    fmt.Println(Factorize(25)) // [5 5]
    fmt.Println(Factorize(70)) // [2 5 7]
}
*/
package main

import (
	"fmt"
)

func Factorize(n int) []int {

	factors := []int{}
	for i := 2; i <= n; i++ {
		if n%i == 0 {
			factors = append(factors, i)
			n = n / i
			i--
		}
		if n == 1 {
			break
		}
	}
	return factors
}

func main() {
	fmt.Println(Factorize(8))  // [2 2 2]
	fmt.Println(Factorize(25)) // [5 5]
	fmt.Println(Factorize(70)) // [2 5 7]
}

/*
import (
	"fmt"
)

// Return list of prime factors of given integer in the order from smallest to largest.
// Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
// Input number should be equal to the product of all factors
// >>> Factorize(8)
// 2, 2, 2
// 2, 2, 2
// 2, 2, 2
// 2, 5, 5
// 2, 5, 5
// 2, 7, 7
func Factorize(n int) []int {
	factors := []int{}
	for i := 2; i <= n; i++ {
		if n%