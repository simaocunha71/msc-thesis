```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst){
        Optional<Integer> largestNegative = Optional.empty();
        Optional<Integer> smallestPositive = Optional.empty();
        for(int num : lst){
            if(num < 0){
                if(largestNegative.isPresent()){
                    largestNegative = Optional.of(Math.max(num, largestNegative.get()));
                }
                else{
                    largestNegative = Optional.of(num);
                }
            }
            else if(num > 0){
                if(smallestPositive.isPresent()){
                    smallestPositive = Optional.of(Math.min(num, smallestPositive.get()));
                }
                else{
                    smallestPositive = Optional.of(num);
                }
            }
        }
        return Arrays.asList(largestNegative, smallestPositive);
    }
}
```