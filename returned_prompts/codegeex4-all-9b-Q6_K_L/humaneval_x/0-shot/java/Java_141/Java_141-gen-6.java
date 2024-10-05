```java
import java.util.*;
import java.lang.*;

class Solution {
    public String filenameCheck(String file_name) {
        // Check for the presence of more than three digits
        if (file_name.chars().filter(Character::isDigit).count() > 3) {
            return "No";
        }

        // Check for the presence of exactly one dot
        if (file_name.chars().filter(ch -> ch == '.').count() != 1) {
            return "No";
        }

        // Check that the substring before the dot starts with a letter from the latin alphabet
        int dotIndex = file_name.indexOf('.');
        if (!Character.isLetter(file_name.charAt(dotIndex - 1))) {
            return "No";
        }

        // Check that the substring after the dot is one of "txt", "exe", "dll"
        String extension = file_name.substring(dotIndex + 1);
        if (!extension.equals("txt") && !extension.equals("exe") && !extension.equals("dll")) {
            return "No";
        }

        return "Yes";
    }
}
```
