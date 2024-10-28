```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> prodSigns(List<Integer> arr) {
        if (arr.size() == 0) return Optional.empty();

        int prod = 1;
        int sign = 1;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) < 0) sign *= -1;
            if (arr.get(i) == 0) return Optional.of(0);
            prod *= Math.abs(arr.get(i));
        }

        return Optional.of(prod * sign);
    }
}
```
