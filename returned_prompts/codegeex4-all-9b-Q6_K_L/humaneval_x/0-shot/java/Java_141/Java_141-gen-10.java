```java
import java.util.*;
import java.lang.*;

class Solution {
    public String filenameCheck(String file_name) {
        String[] parts = file_name.split("\\.", 2);
        if (parts.length != 2) return "No";
        String name = parts[0];
        String extension = parts[1];
        if (!name.matches("^[a-zA-Z][a-zA-Z0-9]*$")) return "No";
        if (!Arrays.asList("txt", "exe", "dll").contains(extension)) return "No";
        if (name.replaceAll("[a-zA-Z]", "").length() > 3) return "No";
        return "Yes";
    }
}
```
