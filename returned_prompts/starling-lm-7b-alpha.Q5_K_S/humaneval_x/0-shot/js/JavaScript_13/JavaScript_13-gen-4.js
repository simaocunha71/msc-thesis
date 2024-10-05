    while (a != 0 && b != 0) {
        if (a > b) {
            a %= b;
        } else {
            b %= a;
        }
    }
    return a + b;
};

// Test cases
console.log(greatestCommonDivisor(3, 5));  // 1
console.log(greatestCommonDivisor(25, 15));  // 5


/*
The Euclidean algorithm can be used to compute the greatest common divisor (GCD) of two integers.
The algorithm is as follows:

    Initialize a and b to the input values.
    While a is not equal to 0 and b is not equal to 0:
        If a is greater than b:
            Set a to the remainder of a divided by b.
        Else:
            Set b to the remainder of b divided by a.
    After the loop, return the value of a.

The Euclidean algorithm is correct because the GCD of two numbers does not change if you divide both numbers by the same value.

In this implementation, we initialize a and b to the input values and enter a while loop.
In the while loop, we check if a is not equal to 0 and b is not equal to 0. If this condition is true, we enter the if statement.
If a is greater than b, we set a to the remainder of a divided by b. Otherwise, we set b to the remainder of b divided by a.
After the while loop, we return the value of a, which is the GCD of the input values.

To test the implementation, we call the function with two pairs of integers and print the results.
The expected outputs are 1 and 5, respectively.


*/



































































































