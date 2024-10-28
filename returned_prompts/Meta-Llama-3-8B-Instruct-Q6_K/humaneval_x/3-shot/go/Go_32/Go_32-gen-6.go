    // Assuming xs has an even number of coefficients
    // and the largest non-zero coefficient is at the beginning
    // (which guarantees a solution)
    // and the polynomial has a root.
    // 
    // We can use Newton-Raphson method to find the root.
    // 
    // We start with an initial guess x0 = 0
    x := 0.0
    for i := 0; i < 100; i++ {
        // calculate the polynomial at x
        p := Poly(xs, x)
        // calculate the derivative of the polynomial
        dp := Poly(xs[:len(xs)-1], x)
        // update x
        x = x - p / dp
    }
    return x
}