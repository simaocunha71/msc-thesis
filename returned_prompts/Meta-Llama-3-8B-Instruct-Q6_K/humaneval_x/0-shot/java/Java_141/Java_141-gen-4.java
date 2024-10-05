```java
import java.util.*;

public class Solution {
    public String filenameCheck(String file_name) {
        if (file_name == null || file_name.length() == 0) {
            return "No";
        }
        
        int dotIndex = file_name.indexOf('.');
        if (dotIndex == -1 || dotIndex == 0 || dotIndex == file_name.length() - 1) {
            return "No";
        }
        
        String beforeDot = file_name.substring(0, dotIndex);
        String afterDot = file_name.substring(dotIndex + 1);
        
        if (!isValidBeforeDot(beforeDot) || !isValidAfterDot(afterDot)) {
            return "No";
        }
        
        return "Yes";
    }
    
    private boolean isValidBeforeDot(String str) {
        if (str.length() == 0 || !isValidLatinLetter(str.charAt(0))) {
            return false;
        }
        
        for (int i = 1; i < str.length(); i++) {
            if (!Character.isLetter(str.charAt(i)) && !Character.isDigit(str.charAt(i))) {
                return false;
            }
        }
        
        return true;
    }
    
    private boolean isValidAfterDot(String str) {
        return "txt".equals(str) || "exe".equals(str) || "dll".equals(str);
    }
    
    private boolean isValidLatinLetter(char c) {
        return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z');
    }
}
```
The code defines a class `Solution` with a method `filenameCheck` that takes a file name as a string and returns "Yes" if the file name is valid, and "No" otherwise.

The method first checks if the file name is null or empty, in which case it returns "No". It then checks if the file name contains exactly one dot, and if the dot is at the beginning or end of the file name, in which case it returns "No".

It then extracts the substring before and after the dot, and checks if the substring before the dot is valid (i.e., starts with a latin letter and contains only letters and digits, and if the substring after the dot is one of the valid extensions ("txt", "exe", or "dll").

The method `isValidBeforeDot` checks if the substring before the dot is valid, and the method `isValidAfterDot` checks if the substring after the dot is one of