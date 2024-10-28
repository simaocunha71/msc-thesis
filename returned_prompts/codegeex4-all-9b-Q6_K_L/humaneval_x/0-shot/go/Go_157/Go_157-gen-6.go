To determine if a triangle is a right-angled triangle, you can use the Pythagorean theorem, which states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. 

Given three sides `a`, `b`, and `c`, where `c` is the hypotenuse (the longest side), the function should return `true` if `a^2 + b^2 = c^2` and `false` otherwise. 

Here's the updated function:

```go
func RightAngleTriangle(a, b, c int) bool {
    // Ensure c is the longest side
    if a > b {
        b, a = a, b
    }
    if a > c {
        c, a = a, c
    }
    if b > c {
        c, b = b, c
    }

    // Check if the sides satisfy the Pythagorean theorem
    return c*c == a*a + b*b
}
```

This function first sorts the sides so that `c` is always the longest side. Then it checks if the equation `c^2 = a^2 + b^2` holds true. If it does, the function returns `true`, indicating that the triangle is right-angled. Otherwise, it returns `false`.