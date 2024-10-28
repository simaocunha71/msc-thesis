        int sum = 0;
        for (int i = 0; i < lst.size(); i++) {
            if (i % 2 == 0 && lst.get(i) % 2 != 0) {
                sum += lst.get(i);
            }
        }
        return sum;
    }
}

This program will iterate through the list of integers and if the index is even and the value at that index is odd, it will add that value to the sum.
*/

// Test the solution
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        // Test case 1
        System.out.println(sol.solution(Arrays.asList(5, 8, 7, 1))); // Expected output: 12

        // Test case 2
        System.out.println(sol.solution(Arrays.asList(3, 3, 3, 3, 3))); // Expected output: 9

        // Test case 3
        System.out.println(sol.solution(Arrays.asList(30, 13, 24, 321))); // Expected output: 0
    }
}
```

The program uses the modulo operator to determine if a number is odd or even. If the index is even and the number is odd, it adds the number to the sum.

The expected outputs are as follows:

- For the first test case, the sum of the odd numbers at even positions is 5 + 1 = 6.
- For the second test case, the sum of the odd numbers at even positions is 3 + 3 + 3 = 9.
- For the third test case, there are no odd numbers at even positions, so the sum is 0.

Therefore, the program will print the correct results.
*/

// Test the solution
public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        // Test case 1
        System.out.println(sol.solution(Arrays.asList(5, 8, 7, 1))); // Ex