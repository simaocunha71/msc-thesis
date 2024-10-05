    for i := 0; i < len(xs)/2; i++ {
        xs[i], xs[len(xs)-i-1] = xs[len(xs)-i-1], xs[i]
    }
    low, high := 0.0, 1.0
    for {
        mid := (low + high) / 2.0
        if Poly(xs, mid) == 0.0 || (Poly(xs, low) * Poly(xs, mid) < 0) {
            high = mid
        } else {
            low = mid
        }
        if math.Abs(Poly(xs, mid)) < 1e-6 {
            return mid
        }
    }
}

My question is: 
Why does the FindZero function in the code above not work correctly, even though it seems to follow the logic of the Bisection Method?

A: The issue lies in the fact that the Bisection Method assumes that there exists at least one root in the interval [a, b]. In your case, there is no guarantee that the function will cross the x-axis at any point in the interval [0, 1]. This is why the Bisection Method might not converge even if there are roots.

The Bisection Method is a root-finding algorithm that applies to any continuous function for which one knows two values with opposite signs.

In your case, the function Poly(xs, x) is a polynomial function, and the coefficients of the polynomial are known. However, it's not guaranteed that the polynomial will cross the x-axis (i.e., have different signs at both ends of the interval) in the interval [0, 1].

The FindZero function is using the Bisection Method to find a root of the polynomial. The function checks if the function crosses the x-axis in the interval [0, 1]. If it does, the Bisection Method is used to find the root. Otherwise, it doesn't find a root.

To fix this, you can modify the FindZero function to first check if the polynomial crosses the x-axis in the interval [0, 1]. If it does, use the Bisection Method to find the root. If it doesn't, the function