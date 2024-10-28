        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}

Solution solution = new Solution();
int result = solution.sumToN(10);
System.out.println(result); // Output: 55

Explanation:
The sumToN function calculates the sum of all numbers from 1 to n. It uses a for loop to iterate from 1 to n, and for each iteration, it adds the current number to the sum. The function returns the calculated sum.

In the example, the sumToN function is called with the argument 10, which means it calculates the sum of all numbers from 1 to 10. The function returns the result, which is 55, and it is printed to the console.

Note that the sumToN function has a time complexity of O(n), where n is the input value, because it uses a linear loop to calculate the sum. This means that the function's running time increases linearly with the input size. For large input values, the function may take a significant amount of time to complete. In such cases, it may be more efficient to use a formula-based approach to calculate the sum, such as the formula for the sum of an arithmetic series. However, for small input values, the for loop approach is sufficient and easy to understand.