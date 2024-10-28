Here is the Java solution to the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean checkDictCase(Map<Object, Object> dict) {
        // Check if the map is empty
        if (dict.isEmpty()) {
            return false;
        }

        // Check if all keys are strings
        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) {
                return false;
            }
        }

        // Check if all keys are in lower case or upper case
        boolean allLowerCase = true;
        boolean allUpperCase = true;

        for (String key : dict.keySet()) {
            if (!key.equals(key.toLowerCase())) {
                allLowerCase = false;
            }

            if (!key.equals(key.toUpperCase())) {
                allUpperCase = false;
            }
        }

        return allLowerCase || allUpperCase;
    }
}
```
This solution first checks if the map is empty. If it is, it returns False. It then checks if all keys are strings. If any key is not a string, it returns False. Finally, it checks if all keys are in lower case or upper case. If all keys are in lower case or all keys are in upper case, it returns True. Otherwise, it returns False.