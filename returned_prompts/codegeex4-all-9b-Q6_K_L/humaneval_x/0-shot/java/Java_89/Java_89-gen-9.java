```java
import java.util.*;
import java.lang.*;

class Solution {
    public String encrypt(String s) {
        String result = "";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int ascii = (int) c;
            if (ascii >= 65 && ascii <= 90) {
                ascii = (ascii - 65 + 2 * 2) % 26 + 65;
            } else if (ascii >= 97 && ascii <= 122) {
                ascii = (ascii - 97 + 2 * 2) % 26 + 97;
            }
            result += (char) ascii;
        }
        return result;
    }
}
```