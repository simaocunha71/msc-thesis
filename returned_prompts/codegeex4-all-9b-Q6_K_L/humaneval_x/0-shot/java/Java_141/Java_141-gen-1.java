```java
import java.util.*;
import java.lang.*;

class Solution {
    public String filenameCheck(String file_name) {
        // Check if the file name contains more than three digits
        int digitCount = 0;
        for (char c : file_name.toCharArray()) {
            if (Character.isDigit(c)) {
                digitCount++;
                if (digitCount > 3) {
                    return "No";
                }
            }
        }

        // Check if the file name contains exactly one dot '.'
        int dotCount = 0;
        for (char c : file_name.toCharArray()) {
            if (c == '.') {
                dotCount++;
                if (dotCount > 1) {
                    return "No";
                }
            }
        }
        if (dotCount != 1) {
            return "No";
        }

        // Check if the substring before the dot starts with a latin alphapet letter
        int dotIndex = file_name.indexOf('.');
        if (dotIndex == 0 || !Character.isLetter(file_name.charAt(dotIndex - 1))) {
            return "No";
        }

        // Check if the substring after the dot is one of ["txt", "exe", "dll"]
        String extension = file_name.substring(dotIndex + 1);
        if (!extension.equals("txt") && !extension.equals("exe") && !extension.equals("dll")) {
            return "No";
        }

        return "Yes";
    }
}
```
