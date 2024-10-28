```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> derivative(List<Integer> xs) {
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i < xs.size(); i++) {
            result.add(xs.get(i) * i);
        }
        return result;
    }
}
```