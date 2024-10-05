Here is the solution for the problem:

```java
import java.util.*;

class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        Map<String, Integer> strengthMap = new HashMap<>();
        for (String extension : extensions) {
            int cap = 0, sm = 0;
            for (char c : extension.toCharArray()) {
                if (Character.isUpperCase(c)) {
                    cap++;
                } else if (Character.isLowerCase(c)) {
                    sm++;
                }
            }
            strengthMap.put(extension, cap - sm);
        }
        int maxStrength = -1;
        String strongestExtension = "";
        for (Map.Entry<String, Integer> entry : strengthMap.entrySet()) {
            if (entry.getValue() > maxStrength) {
                maxStrength = entry.getValue();
                strongestExtension = entry.getKey();
            }
        }
        return class_name + "." + strongestExtension;
    }
}
```

Explanation:
The solution uses a map to store the strength of each extension. It iterates over the extensions and calculates the strength of each extension by counting the number of uppercase and lowercase letters. The strength is then calculated as the difference between the number of uppercase letters and the number of lowercase letters. The extension with the maximum strength is then selected as the strongest extension. If there are multiple extensions with the same strength, the one that comes first in the list is chosen. The strongest extension is then concatenated with the class name to form the final output string.