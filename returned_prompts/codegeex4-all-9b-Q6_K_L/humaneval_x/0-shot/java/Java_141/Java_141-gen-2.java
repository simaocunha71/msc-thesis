```java
import java.util.*;
import java.lang.*;

class Solution {
    public String filenameCheck(String file_name) {
        int dot_count = 0;
        int digit_count = 0;
        String[] valid_extensions = new String[]{"txt", "exe", "dll"};
        boolean starts_with_letter = false;
        for (int i = 0; i < file_name.length(); i++) {
            char c = file_name.charAt(i);
            if (c >= '0' && c <= '9') {
                digit_count += 1;
            } else if (c == '.') {
                dot_count += 1;
            } else if (i == 0 && (c < 'a' || c > 'z') && (c < 'A' || c > 'Z')) {
                return "No";
            }
        }
        if (dot_count != 1 || digit_count > 3) {
            return "No";
        }
        String[] split_name = file_name.split("\\.");
        if (split_name.length != 2) {
            return "No";
        }
        String name = split_name[0];
        String extension = split_name[1];
        if (!Arrays.asList(valid_extensions).contains(extension)) {
            return "No";
        }
        for (int i = 0; i < name.length(); i++) {
            char c = name.charAt(i);
            if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
                starts_with_letter = true;
                break;
            }
        }
        if (starts_with_letter) {
            return "Yes";
        } else {
            return "No";
        }
    }
}
```