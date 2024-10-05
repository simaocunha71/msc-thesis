        if (b == 0) {
            return a;
        } else {
            return greatestCommonDivisor(b, a % b);
        }
    }
}

Here, we use the Euclidean algorithm to find the greatest common divisor (GCD) of two integers a and b.

This algorithm states that the greatest common divisor of two integers a and b is the same as the greatest common divisor of b and a%b (the remainder of a divided by b). This is repeated until b is 0, at which point a is the GCD.

The Euclidean algorithm is based on the principle that the remainder of the Euclidean division of two numbers a and b (denoted a div b with the quotient q and remainder r) uniquely determines the Euclidean division of a by b.

In this case, we're using recursion to implement the Euclidean algorithm.

This function can be tested with a main method like so:

```
public static void main(String[] args) {
    Solution s = new Solution();
    System.out.println(s.greatestCommonDivisor(3, 5)); // prints 1
    System.out.println(s.greatestCommonDivisor(25, 15)); // prints 5
}
```
*/


// ----------------------------------------
// Solution 2: Iterative Solution
// ----------------------------------------

/*
