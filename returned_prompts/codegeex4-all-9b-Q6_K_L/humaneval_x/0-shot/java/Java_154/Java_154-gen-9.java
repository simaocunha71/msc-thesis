```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean cycpatternCheck(String a, String b) {
        if(a.length() < b.length()) {
            return false;
        }

        for(int i = 0; i < a.length(); i++) {
            String rotated = a.substring(i) + a.substring(0, i);
            if(rotated.contains(b)) {
                return true;
            }
        }

        return false;
    }
}
```