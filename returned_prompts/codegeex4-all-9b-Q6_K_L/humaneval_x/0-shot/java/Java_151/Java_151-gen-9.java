```java
import java.util.*;
import java.lang.*;

class Solution {
    public int doubleTheDifference(List<Object> lst) {
        int result = 0;
        for (Object obj : lst) {
            if (obj instanceof Integer) {
                int num = (int) obj;
                if (num > 0 && num % 2 != 0) {
                    result += num * num;
                }
            }
        }
        return result;
    }
}
```