```
    if a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c == a*a {
        return true
    }
    return false
```


Explanation:
In a right-angled triangle, the sum of the squares of the lengths of the two shorter sides is equal to the square of the length of the hypotenuse. This is known as the Pythagorean theorem.
In the code, we first check if the sum of the squares of the lengths of two sides is equal to the square of the length of the third side. If it is, then the three sides form a right-angled triangle and we return true. If not, we return false.