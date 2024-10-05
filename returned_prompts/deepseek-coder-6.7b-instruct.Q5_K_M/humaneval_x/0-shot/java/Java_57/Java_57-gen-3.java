
```java
import java.util.*;
import java.lang.*;

class Solution  {
    public boolean monotonic(List<Integer> l) {
        boolean increasing = true;
        boolean decreasing = true;

        for (int i = 0; i < l.size() - 1; i++) {
            if (l.get(i) < l.get