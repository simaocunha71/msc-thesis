```java
import java.util.*;
import java.lang.*;

class Solution {
    public int canArrange(List<Integer> arr) {
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) <= arr.get(i - 1)) {
                return i - 1;
            }
        }
        return -1;
    }
}
```