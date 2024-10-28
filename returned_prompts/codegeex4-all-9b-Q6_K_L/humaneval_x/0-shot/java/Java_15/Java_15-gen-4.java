```java
import java.util.*;
import java.lang.*;

class Solution {
    public String stringSequence(int n) {
        return IntStream.range(0, n + 1).mapToObj(String::valueOf).collect(Collectors.joining(" "));
    }
}
```