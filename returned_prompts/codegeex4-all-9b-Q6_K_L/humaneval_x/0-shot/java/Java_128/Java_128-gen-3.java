```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        if (arr.isEmpty()) return Optional.empty();
        int sign = 1;
        int sum = 0;
        for (int i : arr) {
            if (i < 0) sign *= -1;
            else if (i == 0) return Optional.of(0);
            sum += Math.abs(i);
        }
        return Optional.of(sign * sum);
    }
}
```