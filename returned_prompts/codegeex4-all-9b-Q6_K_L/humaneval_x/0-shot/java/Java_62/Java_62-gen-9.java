```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> derivative(List<Integer> xs) {
        List<Integer> derivative = new ArrayList<>();
        for (int i = 1; i < xs.size(); i++) {
            derivative.add(xs.get(i) * i);
        }
        return derivative;
    }
}
```