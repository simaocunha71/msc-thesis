```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> listSort(List<String> lst) {
        lst.removeIf(s -> s.length() % 2 != 0);
        Collections.sort(lst, (s1, s2) -> {
            if (s1.length() == s2.length()) {
                return s1.compareTo(s2);
            } else {
                return Integer.compare(s1.length(), s2.length());
            }
        });
        return lst;
    }
}
```