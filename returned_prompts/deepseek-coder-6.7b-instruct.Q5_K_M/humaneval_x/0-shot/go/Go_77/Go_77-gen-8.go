    return a == int(math.Pow(float64(int(math.Pow(float64(a), 1.0/3.0))), 3.0)) || a == int(math.Pow(float64(int(math.Pow(float64(a), 1.0/3.0))+1), 3.0)) || a == int(math.Pow(float64(int(math.Pow(float64(a), 1.0/3.0))-1), 3.0))
}


A: The reason you're getting incorrect results is because the math.Pow function doesn't always return an integer. The problem lies in the fact that the square root of a number can be a fraction.
You can use the math.Round function to round the result to the nearest integer.
Here is a corrected version of your function:

```go
import (
    "math"
)

func Iscube(a int) bool {
    root := int(math.Pow(float64(a), 1.0/3.0))
    return a == int(math.Pow(float64(root), 3.0)) || a == int(math.Pow(float64(root+1), 3.0)) || a == int(math.Pow(float64(root-1), 3.0))
}
```

This function works by first calculating the cube root of the input number, then checking if the number is a perfect cube, or if it is one less or one more than a perfect cube. If either of these conditions is true, the function returns true; otherwise, it returns false.

Note: This function assumes that the input will always be a non-negative integer, as negative numbers cannot be cubed. If you need to handle negative inputs, you'll need to modify the function to handle those cases separately.

In the corrected version of the function, the math.Pow function is used to raise the cube root to the power of 3. This will give you the original number if it is a perfect cube. If the original number is not a perfect cube, but is the result of raising some integer to