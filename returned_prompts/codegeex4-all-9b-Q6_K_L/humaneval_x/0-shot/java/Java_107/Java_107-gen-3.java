```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> evenOddPalindrome(int n) {
        int evenCount = 0;
        int oddCount = 0;
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
        String str = String.valueOf(num);
        int left = 0;
        int right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
```