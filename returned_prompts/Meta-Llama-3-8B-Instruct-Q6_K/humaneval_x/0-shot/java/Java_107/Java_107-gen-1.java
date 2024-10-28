Here is a Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> evenOddPalindrome(int n) {
        int evenCount = 0;
        int oddCount = 0;

        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i) && i % 2 == 0) {
                evenCount++;
            } else if (isPalindrome(i) && i % 2 != 0) {
                oddCount++;
            }
        }

        List<Integer> result = new ArrayList<>();
        result.add(evenCount);
        result.add(oddCount);
        return result;
    }

    public boolean isPalindrome(int n) {
        int reversed = 0;
        int original = n;

        while (n != 0) {
            int remainder = n % 10;
            reversed = reversed * 10 + remainder;
            n /= 10;
        }

        return original == reversed;
    }
}
```

In this solution, we use two counters `evenCount` and `oddCount` to count the number of even and odd integer palindromes respectively. We iterate over the range from 1 to `n` and check if each number is a palindrome using the `isPalindrome` method. If it is a palindrome and even (or odd), we increment the corresponding counter.

The `isPalindrome` method checks if a given integer is a palindrome by reversing the integer and comparing it with the original integer. If they are equal, the integer is a palindrome.

Finally, we create a list `result` and add the `evenCount` and `oddCount` to it, and return the list.

The time complexity of this solution is O(n) because we iterate over the range from 1 to `n` once. The space complexity is O(1) because we use a constant amount of space to store the counters and the result list.