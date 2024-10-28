```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int totalCharCount1 = lst1.stream().mapToInt(String::length).sum();
        int totalCharCount2 = lst2.stream().mapToInt(String::length).sum();

        if (totalCharCount1 < totalCharCount2) {
            return lst1;
        } else if (totalCharCount1 > totalCharCount2) {
            return lst2;
        } else {
            return lst1;
        }
    }
}
```