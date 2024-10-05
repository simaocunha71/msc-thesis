```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> makeAPile(int n) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int current = n;
        for (int i = 0; i < n; i++) {
            result.add(current);
            if (n % 2 == 0) {
                current += 2;
            } else {
                current += 2;
            }
        }
        return result;
    }
}
```