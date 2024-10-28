```java
import java.util.*;
import java.lang.*;

class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        int max = Integer.MIN_VALUE;
        String maxStr = "";
        for (String ext : extensions) {
            int strength = ext.chars().filter(Character::isUpperCase).count() - ext.chars().filter(Character::isLowerCase).count();
            if (strength > max) {
                max = strength;
                maxStr = ext;
            }
        }
        return class_name + "." + maxStr;
    }
}
```