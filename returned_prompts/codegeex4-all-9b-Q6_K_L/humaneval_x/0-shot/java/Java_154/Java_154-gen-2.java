```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean cycpatternCheck(String a, String b) {
        for (int i = 0; i < a.length(); i++) {
            if (a.substring(i).startsWith(b)) {
                return true;
            }
            if (a.substring(0, a.length() - i).startsWith(b)) {
                return true;
            }
        }
        return false;
    }
}
```