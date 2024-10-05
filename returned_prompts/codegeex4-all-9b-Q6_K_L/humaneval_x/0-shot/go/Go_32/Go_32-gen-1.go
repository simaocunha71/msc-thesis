import (
	"fmt"
	"math"
)

// Evaluates polynomial with coefficients xs at point x.
// return xs[0] + xs[1] * x + xs[1] * x^2 + .... xs[n] * x^n
func Poly(xs []int, x float64) float64 {
	sum := 0.0
	for i, coeff := range xs {
		sum += float64(coeff) * math.Pow(x, float64(i))
	}
	return sum
}

// xs are coefficients of a polynomial.
// FindZero find x such that Poly(x) = 0.
// FindZero returns only only zero point, even if there are many.
// Moreover, FindZero only takes list xs having even number of coefficients
// and largest non zero coefficient as it guarantees
// a solution.
// >>> round(FindZero([1, 2]), 2) # f(x) = 1 + 2x
// -0.5
// >>> round(FindZero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
// 1.0
func FindZero(xs []int) float64 {

	// check if xs has even number of elements
	if len(xs)%2 != 0 {
		fmt.Println("xs must have an even number of elements")
		return 0
	}

	// check if xs has a largest non zero coefficient
	maxCoeff := 0
	for _, coeff := range xs {
		if coeff > maxCoeff {
			maxCoeff = coeff
		}
	}
	if maxCoeff == 0 {
		fmt.Println("xs must have a largest non zero coefficient")
		return 0
	}

	// find the zero point
	x := float64(0)
	for i := 0; i < len(xs); i++ {
		x = -xs[i] / float64(len(xs)-i)
		if Poly(xs, x) == 0 {
			return x
		}
	}

	return x
}

func main() {
	fmt.Println(FindZero([]int{1, 2}))             // -0.5
	fmt.Println(FindZero([]int{-6, 11, -6, 1}))    // 1.0
	fmt.Println(FindZero([]int{1