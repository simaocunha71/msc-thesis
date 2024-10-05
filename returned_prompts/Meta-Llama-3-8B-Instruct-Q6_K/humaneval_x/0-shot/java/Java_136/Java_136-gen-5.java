Here is a Java function that solves the problem:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<Optional<Integer>> largestSmallestIntegers(List<Integer> lst){
        List<Optional<Integer>> result = new ArrayList<>();
        
        if(lst.isEmpty()){
            result.add(Optional.empty());
            result.add(Optional.empty());
        } else {
            Optional<Integer> maxNegative = lst.stream().filter(x -> x < 0).max(Comparator.naturalOrder());
            Optional<Integer> minPositive = lst.stream().filter(x -> x > 0).min(Comparator.naturalOrder());
            
            if(maxNegative.isPresent() && minPositive.isPresent()){
                result.add(Optional.empty());
                result.add(minPositive);
            } else if(maxNegative.isPresent()){
                result.add(maxNegative);
                result.add(Optional.empty());
            } else if(minPositive.isPresent()){
                result.add(Optional.empty());
                result.add(minPositive);
            } else {
                result.add(Optional.empty());
                result.add(Optional.empty());
            }
        }
        
        return result;
    }
}
```

This function first checks if the input list is empty. If it is, it returns two empty Optional values. If the list is not empty, it uses Java 8 stream API to find the maximum negative and minimum positive integers in the list. If both exist, it returns the maximum negative integer and the minimum positive integer. If only the maximum negative integer exists, it returns that and an empty Optional value. If only the minimum positive integer exists, it returns an empty Optional value and that. If neither exists, it returns two empty Optional values. The result is returned as a list of two Optional values. 