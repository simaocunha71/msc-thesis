    if len(xs)%2==0 {
        var a float64
        var b float64
        a = float64(xs[len(xs)-1])
        b = float64(xs[len(xs)-2])
        return -b / a
    } else {
        panic("Invalid polynomial")
    }
}  // 1 degree polynomial, the zero point is -b/a. For higher degree polynomials, we can use numerical methods like Newton's method to find the zero point.