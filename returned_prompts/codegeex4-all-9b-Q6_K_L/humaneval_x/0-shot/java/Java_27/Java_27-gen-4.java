```java
import java.util.*;
import java.lang.*;

class Solution {
    public String flipCase(String string) {
        return string.chars().mapToObj(c -> Character.isLowerCase(c) ? Character.toUpperCase(c) : Character.toLowerCase(c)).collect(Collectors.joining());
    }
}
```