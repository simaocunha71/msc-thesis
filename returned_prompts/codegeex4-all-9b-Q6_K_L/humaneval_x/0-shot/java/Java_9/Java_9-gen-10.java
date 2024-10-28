```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> rollingMax(List<Integer> numbers) {
        if (numbers.isEmpty()) {
            return Collections.emptyList();
        }
        List<Integer> result = new ArrayList<>();
        int max = numbers.get(0);
        result.add(max);
        for (int i = 1; i < numbers.size(); i++) {
            int num = numbers.get(i);
            if (num > max) {
                max = num;
            }
            result.add(max);
        }
        return result;
    }
}
```