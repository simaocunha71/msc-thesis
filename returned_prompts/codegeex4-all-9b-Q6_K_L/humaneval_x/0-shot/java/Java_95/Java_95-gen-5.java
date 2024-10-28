Here is the Java code that solves the problem:

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
            if (key instanceof String) {
                String strKey = (String) key;
                if (!strKey.equals(strKey.toLowerCase())) {
                    isLowerCase = false;
                }
                if (!strKey.equals(strKey.toUpperCase())) {
                    isUpperCase = false;
                }
            } else {
                return false;
            }
        }
        return isLowerCase || isUpperCase;
    }
}
```

In this code, we first check if the given map is empty. If it is, we return false. Then we initialize two boolean variables, `isLowerCase` and `isUpperCase`, to true. We iterate over the keys in the given map and check if each key is a string. If it is, we check if it is in lower case or upper case and update the corresponding boolean variable accordingly. If the key is not a string, we return false. Finally, we return true if either `isLowerCase` or `isUpperCase` is true, otherwise we return false.