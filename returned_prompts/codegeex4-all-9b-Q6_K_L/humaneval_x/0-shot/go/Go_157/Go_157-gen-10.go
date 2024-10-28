func RightAngleTriangle(a, b, c int) bool {
	return a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a
}

Explanation:

The Pythagorean theorem states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides. In other words, if a, b, and c are the lengths of the sides of a right-angled triangle, then a^2 + b^2 = c^2.

In this problem, we are given the lengths of the three sides of a triangle and we need to determine if they form a right-angled triangle. To do this, we can use the Pythagorean theorem to check if the square of the length of the longest side is equal to the sum of the squares of the lengths of the other two sides.

We can implement this logic in Go as follows:

```go
func RightAngleTriangle(a, b, c int) bool {
    return a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a
}
```

In this code, we first calculate the squares of the lengths of the sides of the triangle. Then, we use the logical OR operator (`||`) to check if any of the following conditions are true:

- The square of the length of side `a` is equal to the sum of the squares of the lengths of sides `b` and `c`.
- The square of the length of side `b` is equal to the sum of the squares of the lengths of sides `a` and `c`.
- The square of the length of side `c` is equal to the sum of the squares of the lengths of sides `a` and `b`.

If any of these conditions are true, then the sides form a right-angled triangle and we return `true`. Otherwise, we return `false`.

This implementation has a time complexity of O(1) because it performs a fixed number of calculations, regardless of the input size.