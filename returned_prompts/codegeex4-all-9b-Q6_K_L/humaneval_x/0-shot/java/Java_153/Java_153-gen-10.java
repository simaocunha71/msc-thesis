```java
import java.util.*;
import java.lang.*;

class Solution {
    public String StrongestExtension(String class_name, List<String> extensions) {
        String maxStr = extensions.get(0);
        int maxStrength = maxStr.chars().filter(Character::isUpperCase).count() - maxStr.chars().filter(Character::isLowerCase).count();
        for (int i = 1; i < extensions.size(); i++) {
            String str = extensions.get(i);
            int strength = str.chars().filter(Character::isUpperCase).count() - str.chars().filter(Character::isLowerCase).count();
            if (strength > maxStrength) {
                maxStrength = strength;
                maxStr = str;
            }
        }
        return class_name + "." + maxStr;
    }
}
```
