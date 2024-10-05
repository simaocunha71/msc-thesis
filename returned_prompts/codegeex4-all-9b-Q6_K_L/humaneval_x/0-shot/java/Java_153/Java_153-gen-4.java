```java
import java.util.*;
import java.lang.*;

class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        if (extensions.isEmpty()) {
            return class_name;
        }
        int max_strength = Integer.MIN_VALUE;
        String strongest_extension = "";
        for (String extension : extensions) {
            int strength = calculateStrength(extension);
            if (strength > max_strength) {
                max_strength = strength;
                strongest_extension = extension;
            }
        }
        return class_name + "." + strongest_extension;
    }

    private int calculateStrength(String extension) {
        int uppercase_count = 0;
        int lowercase_count = 0;
        for (char c : extension.toCharArray()) {
            if (Character.isUpperCase(c)) {
                uppercase_count++;
            } else if (Character.isLowerCase(c)) {
                lowercase_count++;
            }
        }
        return uppercase_count - lowercase_count;
    }
}
```