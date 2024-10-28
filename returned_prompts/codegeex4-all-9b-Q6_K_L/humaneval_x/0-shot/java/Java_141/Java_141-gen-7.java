```java
import java.util.*;
import java.lang.*;

class Solution {
    public String filenameCheck(String file_name) {
        // Check for more than three digits
        int digit_count = 0;
        for (char c : file_name.toCharArray()) {
            if (Character.isDigit(c)) {
                digit_count++;
                if (digit_count > 3) {
                    return "No";
                }
            }
        }
        
        // Check for exactly one dot
        int dot_count = 0;
        for (char c : file_name.toCharArray()) {
            if (c == '.') {
                dot_count++;
                if (dot_count > 1) {
                    return "No";
                }
            }
        }
        if (dot_count == 0) {
            return "No";
        }
        
        // Check if the substring before the dot is not empty and starts with a latin alphapet letter
        int dot_index = file_name.indexOf('.');
        if (dot_index == 0 || !Character.isLetter(file_name.charAt(dot_index - 1))) {
            return "No";
        }
        
        // Check if the substring after the dot is one of ["txt", "exe", "dll"]
        String extension = file_name.substring(dot_index + 1);
        if (!Arrays.asList("txt", "exe", "dll").contains(extension)) {
            return "No";
        }
        
        return "Yes";
    }
}
```
