Here is the Java code which solves the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> evenOddPalindrome(int n) {
        int evenCount = 0, oddCount = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) {
                    evenCount++;
                } else {
                    oddCount++;
                }
            }
        }
        return Arrays.asList(evenCount, oddCount);
    }

    private boolean isPalindrome(int num) {
        int original = num;
        int reversed = 0;
        while (num > 0) {
            int digit = num % 10;
            reversed = reversed * 10 + digit;
            num /= 10;
        }
        return original == reversed;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.evenOddPalindrome(3)); // Output: [1, 2]
        System.out.println(solution.evenOddPalindrome(12)); // Output: [4, 6]
    }
}
```

This code first initializes two counters, `evenCount` and `oddCount`, to keep track of the number of even and odd palindrome integers. Then it iterates through the range from 1 to n, inclusive, checking if each number is a palindrome. If it is, it increments the appropriate counter. The `isPalindrome` method is used to check if a number is a palindrome. Finally, it returns a list containing the values of `evenCount` and `oddCount`.