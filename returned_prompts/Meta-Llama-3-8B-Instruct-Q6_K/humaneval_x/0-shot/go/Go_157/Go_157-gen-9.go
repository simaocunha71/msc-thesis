```go
func RightAngleTriangle(a, b, c int) bool {
    // Check if any two sides are equal
    if a*a+b*b == c*c || a*a+c*c == b*b || b*b+c*c == a*a {
        return true
    }
    return false
}
```


Explanation:
The problem is asking to check if the given three sides of a triangle can form a right-angled triangle. A right-angled triangle is a triangle where one angle is 90 degrees.

We can solve this problem by using the Pythagorean theorem, which states that the sum of the squares of the lengths of the two shorter sides of a right-angled triangle is equal to the square of the length of the hypotenuse.

In the given function, we iterate over the three sides and check if the sum of the squares of any two sides is equal to the square of the third side. If this condition is met, it means that the three sides can form a right-angled triangle, and we return true. Otherwise, we return false.

For example, in the given example `RightAngleTriangle(3, 4, 5)`, the sum of the squares of the two shorter sides (3 and 4) is equal to the square of the hypotenuse (5), so the function returns true. In the example `RightAngleTriangle(1, 2, 3)`, none of the conditions are met, so the function returns false.