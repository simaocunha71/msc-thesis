```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> derivative(List<Integer> xs) {
        int n = xs.size();
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i < n; i++) {
            result.add(xs.get(i) * i);
        }
        return result;
    }
}
```