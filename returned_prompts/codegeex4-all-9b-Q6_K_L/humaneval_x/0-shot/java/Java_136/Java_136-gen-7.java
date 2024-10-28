```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst){
        Optional<Integer> max = Optional.empty();
        Optional<Integer> min = Optional.empty();
        for (Integer num : lst) {
            if (num < 0 && (!max.isPresent() || num > max.get())) {
                max = Optional.of(num);
            }
            if (num > 0 && (!min.isPresent() || num < min.get())) {
                min = Optional.of(num);
            }
        }
        return Arrays.asList(max, min);
    }
}
```