```java
import java.util.*;
import java.lang.*;

class Solution {
    public String filenameCheck(String file_name) {
        int dotCount = 0;
        int digitCount = 0;
        char[] chars = file_name.toCharArray();
        for (char c : chars) {
            if (Character.isDigit(c)) {
                digitCount++;
            } else if (c == '.') {
                dotCount++;
            }
        }
        if (digitCount > 3 || dotCount != 1) {
            return "No";
        }
        String[] parts = file_name.split("\\.");
        if (parts.length != 2) {
            return "No";
        }
        if (!Character.isLetter(parts[0].charAt(0))) {
            return "No";
        }
        if (!(parts[1].equals("txt") || parts[1].equals("exe") || parts[1].equals("dll"))) {
            return "No";
        }
        return "Yes";
    }
}
```
