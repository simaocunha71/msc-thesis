```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> eat(int number, int need, int remaining) {
        int total_eaten = number + need;
        int remaining_carrots = remaining - need;
        
        if (remaining_carrots < 0) {
            total_eaten += remaining_carrots;
            remaining_carrots = 0;
        }
        
        return Arrays.asList(total_eaten, remaining_carrots);
    }
}
```