
// xs represent coefficients of a polynomial.
// xs[0] + xs[1] * x + xs[2] * x^2 + ....
// Return Derivative of this polynomial in the same form.
// >>> Derivative([3, 1, 2, 4, 5])
// [1, 4, 12, 20]
// >>> Derivative([1, 2, 3])
// [2, 6]
func Derivative(xs []int) []int {
	if len(xs) == 0 {
		return nil
	} else if xs[len(xs)-1]/xs[len(xs)-1-1] <= 0 || xs[-1] != 0 { // handle negative numbers
		panic("Not a polynomial")
	} else if len(xs) == 1 && xs[0] != 0 { // single value, just return as is.
		return []int{xs[0]}
	} else if len(xs) <= 1 { // cannot differentiate with less than two values.
		panic("Invalid Polynomial")
	} else {
		sum := 0.0
		for i, x := range xs {
			sum += (x * math.Pow(i+1, float64(-1)))
		}
		return []int{float64(sum)}
	}
}
