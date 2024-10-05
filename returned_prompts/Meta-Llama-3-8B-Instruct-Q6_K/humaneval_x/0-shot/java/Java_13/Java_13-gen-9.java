        if (b == 0) {
            return a;
        }
        return greatestCommonDivisor(b, a % b);
    }
}

Solution sol = new Solution();
int result = sol.greatestCommonDivisor(25, 15);
System.out.println(result); // Output: 5

Explanation:
This is a recursive solution for the greatest common divisor (GCD) of two integers. The GCD of two numbers a and b is the largest positive integer that divides both a and b without leaving a remainder.

The function `greatestCommonDivisor` takes two integers a and b as input and returns their GCD. The function uses a recursive approach to find the GCD. If b is 0, it means that a is the GCD of a and b, so the function returns a. Otherwise, the function calls itself with b and the remainder of a divided by b, until b is 0.

In the example, the GCD of 25 and 15 is 5. The function calls itself with 15 and 10, then with 10 and 5, and finally with 5 and 0, returning 5 as the GCD.

This solution has a time complexity of O(log(min(a, b))), where min(a, b) is the smaller of the two input integers. This is because the function reduces the problem size by half in each recursive call, until the base case of b being 0 is reached. The space complexity is O(log(min(a, b))), as the maximum depth of the recursion tree is log(min(a, b)).  This solution is efficient and scalable for large input values.