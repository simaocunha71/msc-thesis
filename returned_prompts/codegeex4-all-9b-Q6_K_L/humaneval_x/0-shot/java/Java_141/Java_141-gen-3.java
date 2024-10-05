```java
import java.util.*;
import java.lang.*;

class Solution {
    public String filenameCheck(String file_name) {
        if (file_name == null || file_name.length() == 0) {
            return "No";
        }

        int dotIndex = file_name.indexOf('.');
        if (dotIndex == -1 || dotIndex == 0 || dotIndex == file_name.length() - 1) {
            return "No";
        }

        String[] validExtensions = {"txt", "exe", "dll"};
        String extension = file_name.substring(dotIndex + 1);
        if (!Arrays.asList(validExtensions).contains(extension)) {
            return "No";
        }

        String nameWithoutExtension = file_name.substring(0, dotIndex);
        if (!Character.isLetter(nameWithoutExtension.charAt(0))) {
            return "No";
        }

        int digitCount = 0;
        for (char c : nameWithoutExtension.toCharArray()) {
            if (Character.isDigit(c)) {
                digitCount++;
                if (digitCount > 3) {
                    return "No";
                }
            }
        }

        return "Yes";
    }
}
```