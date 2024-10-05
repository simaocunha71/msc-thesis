```java
import java.util.*;
import java.lang.*;

class Solution {
    public int fruitDistribution(String s, int n) {
        List<Integer> lst = new ArrayList<>();
        for (String i : s.split(" ")) {
            try {
                lst.add(Integer.parseInt(i));
            } catch (NumberFormatException ignored) {
            }
        }
        return n - lst.stream().mapToInt(Integer::intValue).sum();
    }
}
```
