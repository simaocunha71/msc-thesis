```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int len1 = lst1.stream().mapToInt(String::length).sum();
        int len2 = lst2.stream().mapToInt(String::length).sum();
        if (len1 <= len2) {
            return lst1;
        }
        return lst2;
    }
}
```