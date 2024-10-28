Here is the Java solution for the problem:

```java
import java.util.*;

class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        double max_strength = Double.NEGATIVE_INFINITY;
        String strongest_extension = "";
        
        for (String extension : extensions) {
            double strength = getStrength(extension);
            if (strength > max_strength) {
                max_strength = strength;
                strongest_extension = extension;
            }
        }
        
        return class_name + "." + strongest_extension;
    }
    
    private double getStrength(String extension) {
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

In this solution, we first initialize `max_strength` and `strongest_extension` to negative infinity and an empty string respectively. Then, we iterate through each extension in the list, calculate its strength using the `getStrength` method, and update `max_strength` and `strongest_extension` if the current extension's strength is greater than `max_strength`. Finally, we return the strongest extension in the format `ClassName.StrongestExtensionName`.

The `getStrength` method calculates the strength of an extension by counting the number of uppercase and lowercase letters in the extension's name, and returning the difference between the two counts.