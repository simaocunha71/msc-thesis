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
This solution uses two pointers, one starting from the beginning of the string and the other from the end. It compares the characters at these two pointers and moves them towards the center until they meet or cross each other. If at any point the characters don't match, it returns false. If the loop completes without finding any non-matching characters, it returns true.