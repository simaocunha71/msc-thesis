Here is a Java solution for this problem:

```java
import java.util.*;

class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        String result = "";
        int maxStrength = Integer.MIN_VALUE;
        for (String extension : extensions) {
            int cap = 0, sm = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    cap++;
                } else if (Character.isLowerCase(c)) {
                    sm++;
                }
            }
            int strength = cap - sm;
            if (strength > maxStrength) {
                maxStrength = strength;
                result = class_name + "." + extension;
            } else if (strength == maxStrength) {
                result = class_name + "." + extension;
            }
        }
        return result;
    }
}
```

This solution iterates over each extension, counts the number of uppercase and lowercase letters, calculates the strength of the extension, and updates the result if the strength is greater than the current maximum. If the strength is equal to the maximum, it updates the result with the current extension. Finally, it returns the result. The time complexity is O(n), where n is the number of extensions. The space complexity is O(1), as it only uses a constant amount of space.