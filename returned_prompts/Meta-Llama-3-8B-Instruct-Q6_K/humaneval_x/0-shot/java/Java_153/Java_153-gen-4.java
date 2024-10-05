Here is the Java code that implements the described functionality:

```java
import java.util.*;

class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        String strongestExtension = "";
        int strongestStrength = Integer.MIN_VALUE;
        for (String extension : extensions) {
            int cap = 0;
            int sm = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    cap++;
                } else {
                    sm++;
                }
            }
            int strength = cap - sm;
            if (strength > strongestStrength) {
                strongestStrength = strength;
                strongestExtension = extension;
            }
        }
        return class_name + "." + strongestExtension;
    }
}
```
This code initializes the `strongestExtension` variable to an empty string and the `strongestStrength` variable to the minimum possible integer value. It then iterates over each extension in the list. For each extension, it calculates the number of uppercase and lowercase letters and uses these counts to calculate the strength of the extension. If the strength of the current extension is greater than the strongest strength found so far, it updates the strongest strength and the strongest extension. Finally, it returns a string in the format "ClassName.StrongestExtensionName". If there are two or more extensions with the same strength, it chooses the one that comes first in the list. 