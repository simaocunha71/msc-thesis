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
	f := []int{2, 1}
	for i := 1; i < n+1; i++ {
		f = append([]int{}, f...)
		next := 0
		for ; next <= len(f)-1; next++ {
			if f[next] > i {
				break
			}
		}
		if next == len(f)+1 && f[len(f)].IsPrime() {
			return f[len(f)-1]+i
		}
	}

	return 0
}

// IsPrime returns if n is prime.
func (n int) IsPrime() bool {
	if n > math.MaxInt64 {
		return false
	}

	for i := 2; i < int(math.Sqrt(float64(n)))+1; i++ {
		if n%i == 0 {
			return false
		}
	}

	return true
}
