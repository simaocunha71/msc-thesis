    for i  := 1;  i < len(xs)/2 + 1;  i++  {
        for j  := 0;  j < len(xs)/2;  j++  {
            if xs[j]  != 0  {
                xs[j], xs[len(xs)-j-1]  =  xs[len(xs)-j-1], xs[j]
                goto A
            }
        }
        if xs[len(xs)/2]  != 0  {
            return float64(xs[len(xs)/2])
        }
    }
    return 0
}

func main() {
    fmt.Printf("%f\n", FindZero([]int{1, 2}))  // f(x) = x + 2x^2
    fmt.Printf("%f\n", FindZero([]int{-6, 11, -6, 1}))  // f(x) = -6 +11x -6x^2 + x^3
}

What I am trying to do is to find the roots of a polynomial. It seems to work for polynomials of degrees 4 and less, but I can't figure out how to make it work for polynomials of higher degree.
I tried to use the Newton-Raphson method, but it seems I'm doing something wrong.
Here is what I tried to use Newton-Raphson method:
