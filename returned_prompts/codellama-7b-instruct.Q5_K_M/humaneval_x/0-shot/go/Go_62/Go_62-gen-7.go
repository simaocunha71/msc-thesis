
// xs represent coefficients of a polynomial.
// xs[0] + xs[1] * x + xs[2] * x^2 + ....
// Return Derivative of this polynomial in the same form.
// >>> Derivative([3, 1, 2, 4, 5])
// [1, 4, 12, 20]
// >>> Derivative([1, 2, 3])
// [2, 6]
func Derivative(xs []int) []int {
    var result []int
    for i, v := range xs {
        if i == 0 {
            result = append(result, v)
            continue
        }
        result = append(result, v*i)
    }
    return result
}

// xs represent coefficients of a polynomial.
// xs[0] + xs[1] * x + xs[2] * x^2 + ....
// Return Derivative of this polynomial in the same form.
// >>> Derivative([3, 1, 2, 4, 5])
// [1, 4, 12, 20]
// >>> Derivative([1, 2, 3])
// [2, 6]
func Derivative(xs []int) []int {
    var result []int
    for i, v := range xs {
        if i == 0 {
            result = append(result, v)
            continue
        }
        result = append(result, v*i)
    }
    return result
}
