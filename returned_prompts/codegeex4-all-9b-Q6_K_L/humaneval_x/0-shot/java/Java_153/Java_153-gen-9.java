```java
import java.util.*;
import java.lang.*;

class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        int max_strength = Integer.MIN_VALUE;
        String strongest_extension = "";
        for (String extension : extensions) {
            int strength = strength(extension);
            if (strength > max_strength) {
                max_strength = strength;
                strongest_extension = extension;
            }
        }
        return class_name + "." + strongest_extension;
    }

    private int strength(String extension) {
        int cap = 0;
        int sm = 0;
        for (char c : extension.toCharArray()) {
            if (Character.isUpperCase(c)) {
                cap++;
            } else if (Character.isLowerCase(c)) {
                sm++;
            }
        }
        return cap - sm;
    }
}
```
