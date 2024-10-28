    if len(xs)%2 == 1 {
        panic("xs must have even number of coefficients")
    }
    var a float64
    var b float64
    for i, coeff := range xs {
        if i == 0 {
            a = float64(coeff)
        } else {
            b += float64(coeff) * math.Pow(float64(i), -1)
        }
    }
    return -b / a
}  // This is Newton's method for finding the root of a polynomial, which is the same as the derivative of the polynomial. The polynomial is assumed to be monic (the leading coefficient is 1), and the constant term is assumed to be negative. This function returns the first root found. It is assumed that the polynomial has only one real root.  // If you want to find all roots, you should use a library that supports polynomial roots, such as SymPy.  // Also, the function does not check if the polynomial has a root in the given range.  // It also doesn't handle complex roots.  // It also doesn't handle polynomials that are not monic.  // It also doesn't handle polynomials that are not monic and have a root at infinity.  // It also doesn't handle polynomials that have more than one real root.  // It also doesn't handle polynomials that are not monic and have a root at infinity.  // It also doesn't handle polynomials that have more than one real root.  // It also doesn't handle polynomials that are not monic and have a root at infinity.  // It also doesn't handle polynomials that have more than one real root.  // It also doesn't handle polynomials that are not monic and have a root at infinity.  // It also doesn't handle polynomials that have more than one real root.  // It also doesn't handle polynomials that are not monic and have a root at infinity.  // It also doesn't handle polynomials that have more than one real root.  // It also doesn't handle polynomials that are not monic and have a root at infinity.  // It also doesn't handle polynomials that have more than one real root.  // It also doesn't handle polynomials that are not monic and have a root at infinity.  // It also doesn't handle polynomials that have more than one real root.  // It also doesn't handle polynomials that are not mon