    n := len(xs)
    if n%2 != 0 {
        panic("FindZero only takes list xs having even number of coefficients")
    }
    var a int
    for i, x := range xs {
        if x != 0 {
            a = i
            break
        }
    }
    if a >= n/2 {
        panic("FindZero only takes list xs having largest non zero coefficient as it guarantees a solution.")
    }
    x := float64(xs[a])
    for i := a + 1; i < n; i += 2 {
        x = Poly(xs, -x) / float64(xs[i])
    }
    return x
}

In the above code, there is a function called FindZero, which finds the zero point of the polynomial.
However, when I call the FindZero function with the parameter [1, 2], the result is -0.5, which is wrong.
I don't understand why this is the case.
I also tried to use the Poly function to calculate the result, but it also returned the wrong result.

For example, I tried to call Poly(xs, -0.5), but it returned -0.5 instead of 0.

I'm not sure why this is happening, as the result of the function should be 0, and the result of Poly(xs, -0.5) should be 0 as well.

Can anyone help me with this problem, and explain why the result is not correct?

Answer:

The reason you are getting a result of -0.5 instead of 0 is because the Poly function uses math.Pow, which rounds to 0 after 15 digits of precision. This means that when the function is called with x = -0.5, the result is calculated as 0, but it is not accurate enough to represent the exact value of the function.

To fix this, you can use the math.Powf function instead of math.Pow, which uses double precision for its calculations. Here's an example of how you can modify the Poly function to use math.Powf:

```go
func Poly(xs []int, x float64) float64 {