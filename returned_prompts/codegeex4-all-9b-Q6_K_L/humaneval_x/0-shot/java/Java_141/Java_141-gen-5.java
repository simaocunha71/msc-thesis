```java
import java.util.*;
import java.lang.*;

class Solution {
    public String filenameCheck(String file_name) {
        String[] parts = file_name.split("\\.");

        if (parts.length != 2) {
            return "No";
        }

        String name = parts[0];
        String extension = parts[1];

        if (!Character.isLetter(name.charAt(0)) || !name.matches(".*[0-9].*")) {
            return "No";
        }

        if (name.length() - name.replace("0", "").length() > 3) {
            return "No";
        }

        if (!Arrays.asList("txt", "exe", "dll").contains(extension)) {
            return "No";
        }

        return "Yes";
    }
}
```
