        return (a * h) / 2.0;
    }
}

Solution explanation:

This Java solution calculates the area of a triangle given the length of one side (a) and the height (h) of the triangle. The area of a triangle is calculated using the formula: (a * h) / 2.0.

In the code, we define a method `triangleArea` that takes two parameters: `a` and `h`. We then return the result of the formula, which is calculated using the `*` operator for multiplication and the `/` operator for division. The `2.0` is used to ensure that the division is performed as a floating-point operation, which is necessary to produce a decimal result.

The unit test `>>> triangleArea(5, 3)` is used to verify that the method returns the correct result for a triangle with a side length of 5 and a height of 3. The expected result is 7.5, which is the area of the triangle calculated using the formula.