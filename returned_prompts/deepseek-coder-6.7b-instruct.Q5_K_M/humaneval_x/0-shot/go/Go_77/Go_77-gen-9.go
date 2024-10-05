    c := int(math.Cbrt(float64(a)))
    return c*c*c == a
}


A: Here's another way to do it:

```go
import "math"

func isCube(n int) bool {
    nAbs := int(math.Abs(float64(n)))
    return nAbs == int(math.Pow(float64(nAbs), 1.0/3))*int(math.Pow(float64(nAbs), 1.0/3))*int(math.Pow(float64(nAbs), 1.0/3))
}
```

This function first gets the absolute value of the input number (to handle negative numbers). Then it calculates the cube root of the absolute value (converting it to an integer, since cube roots are always integers). If the cube of the cube root equals the original number, then the original number is a cube.

This function uses the `math.Abs` function to get the absolute value of a number, the `math.Pow` function to raise a number to a power, and the `int` function to convert a float64 to an integer.

This function assumes that the input is always valid and does not check for invalid input.

For example, the function `isCube(27)` would return `true`, because 27 is a cube of 3, and `isCube(-27)` would also return `true`, because the absolute value of -27 is a cube of 3. The function `isCube(18)` would return `false`, because 18 is not a cube of any integer.

Note: This function uses `math.Pow`