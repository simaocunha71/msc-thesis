```java
import java.util.*;
import java.lang.*;

class Solution {
    public String stringSequence(int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= n; i++) {
            sb.append(i);
            if (i != n) {
                sb.append(" ");
            }
        }
        return sb.toString();
    }
}
```