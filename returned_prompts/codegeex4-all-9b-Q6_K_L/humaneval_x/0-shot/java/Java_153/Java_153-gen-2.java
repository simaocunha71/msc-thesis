```java
import java.util.*;
import java.lang.*;

class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        int maxStrength = Integer.MIN_VALUE;
        String strongestExtension = "";
        for (String extension : extensions) {
            int strength = calculateStrength(extension);
            if (strength > maxStrength) {
                maxStrength = strength;
                strongestExtension = extension;
            }
        }
        return class_name + "." + strongestExtension;
    }

    private int calculateStrength(String extension) {
        int capitalCount = 0;
        int smallCount = 0;
        for (char c : extension.toCharArray()) {
            if (Character.isUpperCase(c)) {
                capitalCount++;
            } else if (Character.isLowerCase(c)) {
                smallCount++;
            }
        }
        return capitalCount - smallCount;
    }
}
```