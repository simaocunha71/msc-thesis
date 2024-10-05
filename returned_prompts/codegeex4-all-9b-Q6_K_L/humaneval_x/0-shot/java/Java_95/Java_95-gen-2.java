```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean checkDictCase(Map<Object, Object> dict) {
        if (dict.isEmpty()) {
            return false;
        }
        boolean isLowerCase = true;
        boolean isUpperCase = true;

        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) {
                return false;
            }
            String strKey = (String) key;
            if (!strKey.equals(strKey.toLowerCase())) {
                isLowerCase = false;
            }
            if (!strKey.equals(strKey.toUpperCase())) {
                isUpperCase = false;
            }
        }

        return isLowerCase || isUpperCase;
    }
}
```