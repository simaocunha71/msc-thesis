```java
import java.util.*;
import java.lang.*;

class Solution {
    public String filenameCheck(String file_name) {
        if (file_name == null) return "No";
        if (file_name.indexOf(".") == -1) return "No";
        if (file_name.indexOf(".") != file_name.lastIndexOf(".")) return "No";
        if (!Character.isLetter(file_name.charAt(0))) return "No";
        if (file_name.split("\\.").length != 2) return "No";
        String[] parts = file_name.split("\\.");
        if (parts[0].length() > 3 || !parts[1].equals("txt") && !parts[1].equals("exe") && !parts[1].equals("dll")) {
            return "No";
        }
        for (char c : parts[0].toCharArray()) {
            if (!Character.isDigit(c) && !Character.isLetter(c)) {
                return "No";
            }
        }
        return "Yes";
    }
}
```