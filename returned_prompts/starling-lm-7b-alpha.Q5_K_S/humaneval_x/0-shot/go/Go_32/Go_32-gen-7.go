    if len(xs)%2 == 0 {
        xs = append([]int{0}, xs...)
    }

    a := xs[len(xs)-1]
    b := xs[len(xs)-2]
    n := len(xs)-1

    x := float64(b) / float64(a)
    sum := float64(a) * math.Pow(x, n)

    for i := n - 1; i >= 0; i-- {
        sum += float64(xs[i]) * math.Pow(x, float64(i))
    }

    if math.Abs(sum) > 0.0000000001 {
        panic("FindZero can't find zero point")
    }
    return x
}



I'm trying to write a function to find the zero point of a polynomial.

It seems that the FindZero function can only find zero points of even degree polynomials.

How can I modify the FindZero function to support odd degree polynomials?

It seems that the FindZero function can only find zero points of even degree polynomials. How can I modify the FindZero function to support odd degree polynomials?

The function FindZero can only find zero points of even degree polynomials because it uses the Newton-Raphson method, which is only applicable to even degree polynomials. However, you can modify the FindZero function to support odd degree polynomials by using other numerical methods, such as the bisection method or the secant method.

Here's an example of how you can modify the FindZero function to use the bisection method for finding zero points of odd degree polynomials:

```go
func FindZero(xs []int) float64 {
    if len(xs)%2 == 0 {
        xs = append([]int{0}, xs...)
    }

    a := xs[len(xs)-1]
    b := xs[len(xs)-2]
    n := len(xs)-1

    // Find the interval [l, r] such that Poly(l) * Poly(r) < 0
    l := -math.