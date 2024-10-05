```go
import (
	"math"
)

// Return list of prime factors of given integer in the order from smallest to largest.
// Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
// Input number should be equal to the product of all factors
func Factorize(n int) []int {
	var factors []int
	for i := 2; i <= int(math.Sqrt(float64(n))+1); i++ {
		if n%i == 0 {
			count := 0
			for n%i == 0 {
				n /= i
				count++
			}
			factors = append(factors, i)
			factors = append(factors, count)
		}
	}
	if n > 1 {
		factors = append(factors, n)
	}
	return factors
}
```