```java
import java.util.*;
import java.lang.*;

class Solution {
    public boolean cycpatternCheck(String a, String b) {
        return a.contains(b) || a.contains(new StringBuilder(b).reverse().toString());
    }
}
```