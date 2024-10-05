```java
import java.util.*;

class Solution {
    public List<Integer> eat(int number, int need, int remaining) {
        List<Integer> result = new ArrayList<>();
        int total = number + need;
        int left = remaining - (need - number);
        result.add(total);
        result.add(left > 0 ? left : 0);
        return result;
    }
}
```

Explanation:
The problem can be solved by first calculating the total number of carrots eaten after the meals (total = number + need). Then, we calculate the number of carrots left after the meals by subtracting the number of carrots eaten from the remaining carrots (left = remaining - (need - number)). If the number of carrots left is negative, we set it to 0. Finally, we return a list containing the total number of carrots eaten and the number of carrots left.