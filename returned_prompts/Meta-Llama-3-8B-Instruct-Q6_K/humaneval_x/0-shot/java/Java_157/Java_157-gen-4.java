        // Write your solution here
        if(a*a+b*b==c*c || a*a+c*c==b*b || b*b+c*c==a*a) {
            return true;
        }
        return false;
    }
}

S:
The problem is asking whether a given triangle with side lengths a, b, and c forms a right-angled triangle or not. A right-angled triangle is a triangle in which one angle is right angle or 90 degree. 

In a right-angled triangle, the square of the hypotenuse side is equal to the sum of squares of the other two sides. This is known as the Pythagorean theorem.

Here is the solution:

```java
public boolean rightAngleTriangle(int a, int b, int c) {
    // If a^2 + b^2 = c^2, it's a right triangle
    if(a*a+b*b==c*c) {
        return true;
    }
    // If a^2 + c^2 = b^2, it's a right triangle
    if(a*a+c*c==b*b) {
        return true;
    }
    // If b^2 + c^2 = a^2, it's a right triangle
    if(b*b+c*c==a*a) {
        return true;
    }
    // If none of the above conditions are met, it's not a right triangle
    return false;
}
```

This solution checks all three possible combinations of the Pythagorean theorem and returns true if any of them are true, and false otherwise. 

For example, if the input is (3, 4, 5), the function will return true because 3^2 + 4^2 = 5^2, which is a right-angled triangle. If the input is (1, 2, 3), the function will return false because none of the above conditions are met. 