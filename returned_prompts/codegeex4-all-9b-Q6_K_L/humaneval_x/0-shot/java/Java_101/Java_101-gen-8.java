```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> wordStrings(String s) {
        return Arrays.asList(s.replaceAll(",", "").split(" "));
    }
}
```