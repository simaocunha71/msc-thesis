```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> intersperse(List<Integer> numbers, int delimiter) {
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < numbers.size(); i++) {
            if (i > 0) {
                res.add(delimiter);
            }
            res.add(numbers.get(i));
        }
        return res;
    }
}
```