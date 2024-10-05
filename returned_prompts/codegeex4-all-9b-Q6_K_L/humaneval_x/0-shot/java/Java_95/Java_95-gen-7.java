```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean checkDictCase(Map<Object, Object> dict) {
        boolean allLowerCase = true;
        boolean allUpperCase = true;

        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) {
                return false;
            }
            String keyStr = (String) key;
            if (!keyStr.equals(keyStr.toLowerCase())) {
                allLowerCase = false;
            }
            if (!keyStr.equals(keyStr.toUpperCase())) {
                allUpperCase = false;
            }
        }

        return allLowerCase || allUpperCase;
    }
}
```