```java
import java.util.*;
import java.lang.*;

class Solution {
    public int canArrange(List<Integer> arr) {
        int count = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) >= arr.get(i - 1)) {
                count++;
            }
        }
        if (count == arr.size() - 1) {
            return arr.size() - 1;
        } else {
            return -1;
        }
    }
}
```