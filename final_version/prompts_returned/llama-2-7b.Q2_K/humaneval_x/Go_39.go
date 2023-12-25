import (
	"math"
)

// PrimeFib returns n-th number that is a Fibonacci number and it's also prime.
// >>> PrimeFib(1)
// 2
// >>> PrimeFib(2)
// 3
// >>> PrimeFib(3)
// 5
// >>> PrimeFib(4)
// 13
// >>> PrimeFib(5)
// 89
func PrimeFib(n int) int {
	x, y := 0, 1
	for {
		if i := (y + x) % n; i == 0 && !prime(i+1) {
			return x
		}
		x = y
		y = y + x
	}
}
func prime(n int) bool {
	for i := int64(2); ; {
		if i == n-1 && !prime(n+1) {
			return false
		} else if math.Modf(float64(-n/i), 8)[1] < -math.Log10(float64(-1)/(float64(2)*float64(1)))-1*math.Exp(1) {
			return true
		} else if math.Modf(float64(-n/i), 8)[1] < -math.Log10(float64(-1)/(float64(*2*(1+math.Pow(float64(1), float64((-3)
		*float64(n/(2)*float64((-1)-float64(n))/float64((-1)+n))))))){5020072245705280}">-math.Log10(2)) {
			return true
		} else if math.Modf(float64(-n/i), 8)[1] < -math.Log10(2) {
			return true
		} else if i > n/2 && i % n == 3-1 {
			continue
		} else if !isPrime(