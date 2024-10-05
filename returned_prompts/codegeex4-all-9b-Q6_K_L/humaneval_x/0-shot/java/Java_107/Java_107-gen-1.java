Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> evenOddPalindrome(int n) {
        int even = 0, odd = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0)
                    even++;
                else
                    odd++;
            }
        }
        return Arrays.asList(even, odd);
    }

    private boolean isPalindrome(int num) {
        int originalNum = num;
        int reverse = 0;
        while (num != 0) {
            int remainder = num % 10;
            reverse = reverse * 10 + remainder;
            num /= 10;
        }
        return originalNum == reverse;
    }
}
```

This solution first initializes two counters, `even` and `odd`, to keep track of the number of even and odd palindromes. Then it iterates from 1 to `n`, checking each number to see if it is a palindrome. If it is, it checks if the number is even or odd and increments the corresponding counter. Finally, it returns a list containing the number of even and odd palindromes.