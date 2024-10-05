```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean checkDictCase(Map<Object, Object> dict) {
        if (dict.isEmpty()) return false;
        boolean isLower = true;
        boolean isUpper = true;
        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) {
                return false;
            }
            String sKey = (String) key;
            if (!sKey.equals(sKey.toLowerCase())) {
                isLower = false;
            }
            if (!sKey.equals(sKey.toUpperCase())) {
                isUpper = false;
            }
        }
        return isLower || isUpper;
    }
}
```