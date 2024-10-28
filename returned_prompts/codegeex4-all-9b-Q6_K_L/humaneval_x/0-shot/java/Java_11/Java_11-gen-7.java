```java
import java.util.*;
import java.lang.*;

class Solution {
    public String stringXor(String a, String b) {
        StringBuilder xor = new StringBuilder();
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) == b.charAt(i)) {
                xor.append("0");
            } else {
                xor.append("1");
            }
        }
        return xor.toString();
    }
}
```
