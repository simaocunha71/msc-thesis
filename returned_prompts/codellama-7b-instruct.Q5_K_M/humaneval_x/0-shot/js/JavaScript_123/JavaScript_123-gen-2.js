
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
	}
	if len(xs) == 1 {
		return nil
	}
	derivative := make([]int, len(xs)-1)
	for i := 0; i < len(derivative); i++ {
		derivative[i] = xs[i+1] * (i + 1)
	}
	return derivative
}

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
	}
	if len(xs) == 1 {
		return nil
	}
	derivative := make([]int, len(xs)-1)
	for i := 0; i < len(derivative); i++ {
		derivative[i] = xs[i+1] * (i + 1)
	}
	return derivative
}

// xs represent coefficients of a polynomial.
// xs[0] + xs[1] * x + xs[2] * x^2 + ....
// Return Derivative of this polynomial in the same form.
// >>> Derivative([3, 1