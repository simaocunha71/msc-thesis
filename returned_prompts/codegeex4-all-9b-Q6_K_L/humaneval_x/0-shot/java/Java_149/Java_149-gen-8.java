```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> listSort(List<String> lst) {
        lst.removeIf(s -> s.length() % 2 != 0);
        lst.sort(Comparator.comparingInt(String::length).thenComparing(String::compareTo));
        return lst;
    }
}
```