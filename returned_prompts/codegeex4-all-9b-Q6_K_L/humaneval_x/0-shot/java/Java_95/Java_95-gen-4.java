Here is a simple Java solution using the Character class:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean checkDictCase(Map<Object, Object> dict) {
        if (dict.isEmpty()) {
            return false;
        }

        boolean isLower = true;
        boolean isUpper = true;

        for (Map.Entry<Object, Object> entry : dict.entrySet()) {
            if (!(entry.getKey() instanceof String)) {
                return false;
            }

            String key = (String) entry.getKey();

            if (!key.chars().allMatch(Character::isLowerCase)) {
                isLower = false;
            }

            if (!key.chars().allMatch(Character::isUpperCase)) {
                isUpper = false;
            }
        }

        return isLower || isUpper;
    }
}
```

This solution iterates over all key-value pairs in the given dictionary. If any key is not a string, it immediately returns false. Then, for each string key, it checks whether all characters are in lower or upper case, and sets the corresponding boolean variable to false if there is any character that does not match the case. Finally, it returns true if at least one of the boolean variables is still true, indicating that all keys are either in lower or upper case, and false otherwise.