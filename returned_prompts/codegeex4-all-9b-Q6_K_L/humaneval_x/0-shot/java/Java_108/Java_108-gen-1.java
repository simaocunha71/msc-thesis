Here is the solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int countNums(List<Integer> arr) {
        int count = 0;
        for (int num : arr) {
            if (countDigits(num) > 0) {
                count++;
            }
        }
        return count;
    }

    private int countDigits(int num) {
        int sum = 0;
        boolean negative = false;
        if (num < 0) {
            num = -num;
            negative = true;
        }
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        if (negative) {
            sum = -sum;
        }
        return sum;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.countNums(Arrays.asList())); // 0
        System.out.println(solution.countNums(Arrays.asList(-1, 11, -11))); // 1
        System.out.println(solution.countNums(Arrays.asList(1, 1, 2))); // 3
    }
}
```

Explanation:
1. The `countNums` function takes a list of integers as input and returns the number of elements which have a sum of digits > 0.
2. It iterates over each number in the list and calls the `countDigits` function to calculate the sum of digits of the number.
3. If the sum of digits > 0, it increments the count.
4. Finally, it returns the count.
5. The `countDigits` function takes an integer as input and returns the sum of its digits.
6. It first checks if the number is negative and stores it in a boolean variable.
7. If the number is negative, it converts it to a positive number.
8. Then, it iterates over each digit of the number and adds it to the sum.
9. If the number was negative, it converts the sum to a negative number.
10. Finally, it returns the sum.
11. In the `main` function, we create an instance of the `Solution` class and call the `countNums` function with different lists of integers to test the solution.