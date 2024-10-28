```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isPalindrome(String text) {
        if (text == null || text.isEmpty()) {
            return true;
        }
        int left = 0;
        int right = text.length() - 1;
        while (left < right) {
            if (text.charAt(left) != text.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
```