```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> makeAPile(int n) {
        List<Integer> result = new ArrayList<>();
        int stones = n;
        for (int i = 0; i < n; i++) {
            result.add(stones);
            if (stones % 2 == 0) {
                stones += 2;
            } else {
                stones += 2;
            }
        }
        return result;
    }
}
```