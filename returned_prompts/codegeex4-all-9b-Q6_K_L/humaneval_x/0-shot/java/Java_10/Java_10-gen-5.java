```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean isPalindrome(String string) {
        int i = 0;
        int j = string.length() - 1;
        while (i < j) {
            if (string.charAt(i)!= string.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    public String makePalindrome(String string) {
        if (isPalindrome(string)) {
            return string;
        }
        int i = 0;
        int j = string.length() - 1;
        while (j >= 0) {
            if (isPalindrome(string.substring(i, j + 1))) {
                break;
            }
            j--;
        }
        String postfix = string.substring(j + 1);
        String prefix = string.substring(0, i);
        return string + new StringBuilder(prefix).reverse().toString() + postfix;
    }
}
```