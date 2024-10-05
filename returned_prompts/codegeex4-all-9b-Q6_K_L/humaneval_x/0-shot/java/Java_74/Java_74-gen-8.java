```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int totalChars1 = lst1.stream().mapToInt(s -> s.length()).sum();
        int totalChars2 = lst2.stream().mapToInt(s -> s.length()).sum();
        if (totalChars1 <= totalChars2) {
            return lst1;
        } else {
            return lst2;
        }
    }
}
```