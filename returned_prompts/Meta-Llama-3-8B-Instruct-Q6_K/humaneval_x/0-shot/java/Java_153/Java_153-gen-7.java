Here is a Java solution using a simple loop to iterate through the extensions and calculate their strengths.

```java
import java.util.*;

class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        String strongestExtension = "";
        int strongestExtensionStrength = 0;
        
        for (String extension : extensions) {
            int cap = 0, sm = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    cap++;
                } else if (Character.isLowerCase(c)) {
                    sm++;
                }
            }
            int extensionStrength = cap - sm;
            if (extensionStrength > strongestExtensionStrength) {
                strongestExtension = extension;
                strongestExtensionStrength = extensionStrength;
            }
        }
        return class_name + "." + strongestExtension;
    }
}
```

In this solution, we first initialize `strongestExtension` and `strongestExtensionStrength` to empty string and 0 respectively. Then we iterate through the extensions and for each extension, we calculate the number of uppercase letters (`cap`) and lowercase letters (`sm`). The strength of the extension is calculated as `cap - sm`. If the strength of the current extension is greater than the strongest extension found so far, we update `strongestExtension` and `strongestExtensionStrength`. Finally, we return the class name followed by the strongest extension. If there are multiple extensions with the same strength, the one that comes first in the list will be chosen. 