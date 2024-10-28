```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> generateIntegers(int a, int b) {
        List<Integer> result = new ArrayList<>();
        for (int i = a; i <= b; i++) {
            if (i % 2 == 0) {
                result.add(i);
            }
        }
        Collections.sort(result);
        return result;
    }
}
```