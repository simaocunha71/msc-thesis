```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst){
        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();
        for(Integer i : lst){
            if(i < 0){
                if(!largestNegative.isPresent() || i > largestNegative.get()){
                    largestNegative = Optional.of(i);
                }
            } else if(i > 0){
                if(!smallestPositive.isPresent() || i < smallestPositive.get()){
                    smallestPositive = Optional.of(i);
                }
            }
        }
        return Arrays.asList(largestNegative, smallestPositive);
    }
}
```