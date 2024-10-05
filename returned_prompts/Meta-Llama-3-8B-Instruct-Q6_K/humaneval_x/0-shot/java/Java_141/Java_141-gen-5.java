```java
import java.util.*;
import java.lang.*;

class Solution {
    public String filenameCheck(String file_name) {

        String[] extensions = {"txt", "exe", "dll"};
        String[] parts = file_name.split("\\.");
        if(parts.length != 2) {
            return "No";
        }
        if(parts[0].isEmpty()) {
            return "No";
        }
        if(!isValidPart(parts[0])) {
            return "No";
        }
        if(!isValidExtension(parts[1])) {
            return "No";
        }
        return "Yes";
    }

    public boolean isValidPart(String part) {
        if(part.isEmpty()) {
            return false;
        }
        if(!part.matches("^[a-zA-Z].*")) {
            return false;
        }
        return part.matches("^[a-zA-Z0-9]*$") && part.length() <= 3;
    }

    public boolean isValidExtension(String extension) {
        String[] validExtensions = {"txt", "exe", "dll"};
        for(String validExtension : validExtensions) {
            if(validExtension.equals(extension)) {
                return true;
            }
        }
        return false;
    }
}
```