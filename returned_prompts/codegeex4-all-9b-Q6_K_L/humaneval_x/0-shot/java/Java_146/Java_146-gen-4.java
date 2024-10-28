```java
import java.util.*;
import java.lang.*;

class Solution {
    public int specialFilter(List<Integer> nums) {
        return (int) nums.stream()
                .filter(n -> n > 10 && Integer.toString(Math.abs(n)).matches("^1[13579]|[13579]1$"))
                .count();
    }
}
```