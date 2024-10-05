```java
import java.util.*;
import java.lang.*;

class Solution {
    public String filenameCheck(String file_name) {
        if (file_name.contains("..")) {
            return "No";
        }
        int dot_index = file_name.indexOf('.');
        if (dot_index == -1 || dot_index == 0 || dot_index == file_name.length() - 1) {
            return "No";
        }
        String prefix = file_name.substring(0, dot_index);
        String suffix = file_name.substring(dot_index + 1);
        if (!suffix.matches("txt|exe|dll")) {
            return "No";
        }
        if (!prefix.matches("[a-zA-Z]\\w*")) {
            return "No";
        }
        int digit_count = 0;
        for (char c : prefix.toCharArray()) {
            if (Character.isDigit(c)) {
                digit_count += 1;
            }
        }
        if (digit_count > 3) {
            return "No";
        }
        return "Yes";
    }
}
```