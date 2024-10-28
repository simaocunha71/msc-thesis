
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
		return make([]int, 0)
	}
	if len(xs) == 2 {
		return []int{xs[1]}
	}
	n := len(xs) - 1
	ys := make([]int, n)
	for i := 1; i < n; i++ {
		ys[i-1] = i * xs[i]
	}
	return ys
}
