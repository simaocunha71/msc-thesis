```java
import java.util.*;

class Solution {
    public boolean checkDictCase(Map<Object, Object> dict) {
        if (dict.isEmpty()) return false;
        boolean isLower = true;
        boolean isUpper = true;
        for (Object key : dict.keySet()) {
            if (!(key instanceof String)) {
                return false;
            }
            String s = (String) key;
            if (!s.equals(s.toLowerCase())) isLower = false;
            if (!s.equals(s.toUpperCase())) isUpper = false;
        }
        return isLower || isUpper;
    }
}
```