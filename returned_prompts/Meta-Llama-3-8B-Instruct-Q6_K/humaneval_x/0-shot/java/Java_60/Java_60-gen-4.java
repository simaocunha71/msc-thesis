        int sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }
}

Solution solution = new Solution();
int result = solution.sumToN(10);
System.out.println(result); // prints 55
// Output: 55
Solution solution1 = new Solution();
int result1 = solution1.sumToN(100);
System.out.println(result1); // prints 5050
// Output: 5050
Solution solution2 = new Solution();
int result2 = solution2.sumToN(5);
System.out.println(result2); // prints 15
// Output: 15
Solution solution3 = new Solution();
int result3 = solution3.sumToN(1);
System.out.println(result3); // prints 1
// Output: 1
Solution solution4 = new Solution();
int result4 = solution4.sumToN(30);
System.out.println(result4); // prints 465
// Output: 465
// Time complexity: O(n)
// Space complexity: O(1) (not counting the input) 





Explanation:
The provided code defines a function called `sumToN` that calculates the sum of all numbers from 1 to a given integer `n`. The function uses a for loop to iterate from 1 to `n` and add each number to a running total `sum`. The function then returns the total sum.

The code also includes a main method that creates instances of the `Solution` class and calls the `sumToN` method with different input values. The results are then printed to the console.

The time complexity of this code is O(n) because the function iterates `n` times to calculate the sum. The space complexity is O(1) because the function only uses a constant amount of space to store the running total and the input value `n`.