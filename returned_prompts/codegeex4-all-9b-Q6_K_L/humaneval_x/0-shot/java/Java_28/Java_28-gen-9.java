```java
import java.util.*;
import java.lang.*;

class Solution {
    public String concatenate(List<String> strings) {
        return strings.stream().collect(Collectors.joining());
    }
}
```