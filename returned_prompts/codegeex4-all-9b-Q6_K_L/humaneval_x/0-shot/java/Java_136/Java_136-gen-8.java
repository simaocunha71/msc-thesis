```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst){
        Optional<Integer> largest = Optional.empty();
        Optional<Integer> smallest = Optional.empty();
        for (int i : lst) {
            if (i < 0 && (!largest.isPresent() || i > largest.get())) {
                largest = Optional.of(i);
            }
            if (i > 0 && (!smallest.isPresent() || i < smallest.get())) {
                smallest = Optional.of(i);
            }
        }
        return Arrays.asList(largest, smallest);
    }
}
```