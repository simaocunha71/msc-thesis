
// xs represent coefficients of a polynomial.
// xs[0] + xs[1] * x + xs[2] * x^2 + ....
// Return Derivative of this polynomial in the same form.
// >>> Derivative([3, 1, 2, 4, 5])
// [1, 4, 12, 20]
// >>> Derivative([1, 2, 3])
// [2, 6]
func Derivative(xs []int) []int {
	if len(xs) == 0 {
		return []int{}
	}

	var m int = len(xs) - 1

	for i := 0; i <= m; i++ {
		a := xs[i]
		b := a + xs[i+1]*2
		c := b + xs[i+2]*3
		// 每次都从上一个结点开始，所以需要循环遍历两次.
		xs = append(xs, c)
	}

	return xs[:m]
}
