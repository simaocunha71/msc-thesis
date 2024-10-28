```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> evenOddPalindrome(int n) {
        int even = 0, odd = 0;
        for (int i = 1; i <= n; i++) {
            if (isPalindrome(i)) {
                if (i % 2 == 0) {
                    even++;
                } else {
                    odd++;
                }
            }
        }
        return Arrays.asList(even, odd);
    }

    private boolean isPalindrome(int x) {
        String s = String.valueOf(x);
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
```