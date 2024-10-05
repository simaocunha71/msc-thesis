Here is a Java solution using two counters for even and odd palindromes:

```java
import java.util.*;

class Solution {
    public List<Integer> evenOddPalindrome(int n) {
        List<Integer> result = new ArrayList<>();
        int evenCount = 0;
        int oddCount = 0;

        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i) && i % 2 == 0) {
                evenCount++;
            } else if (isPalindrome(i) && i % 2 != 0) {
                oddCount++;
            }
        }

        result.add(evenCount);
        result.add(oddCount);
        return result;
    }

    public boolean isPalindrome(int num) {
        int original = num;
        int reversed = 0;
        while (num > 0) {
            int digit = num % 10;
            reversed = reversed * 10 + digit;
            num /= 10;
        }
        return original == reversed;
    }
}
```

This solution iterates over the range from 1 to n, checks if each number is a palindrome using the `isPalindrome` helper method, and then increments either the `evenCount` or `oddCount` depending on the parity of the number. Finally, it returns a list containing the counts of even and odd palindromes.

The `isPalindrome` method checks if a given number is a palindrome by reversing the number and comparing it with the original. It does this by repeatedly extracting the last digit of the number, adding it to the reversed number, and then removing the last digit from the original number. If the reversed number is equal to the original number, then the number is a palindrome. Otherwise, it is not.