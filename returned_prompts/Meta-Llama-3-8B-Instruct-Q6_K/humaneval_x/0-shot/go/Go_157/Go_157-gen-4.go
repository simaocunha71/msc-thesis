```go
func RightAngleTriangle(a, b, c int) bool {
    // your code here
    // if a^2 + b^2 = c^2, then it is a right-angled triangle
    return a*a+b*b == c*c
}
```

Explanation:
The code checks if the given sides `a`, `b`, and `c` form a right-angled triangle by applying the Pythagorean theorem. If the sum of the squares of the two shorter sides is equal to the square of the longest side, then the triangle is right-angled. This is because the Pythagorean theorem states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. In this case, `a` and `b` are the shorter sides and `c` is the longest side. If the condition `a*a+b*b == c*c` is true, then the triangle is right-angled, and the function returns `true`. Otherwise, it returns `false`.