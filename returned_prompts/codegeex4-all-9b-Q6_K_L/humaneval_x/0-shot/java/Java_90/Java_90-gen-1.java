```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst.size() < 2) {
            return Optional.empty();
        }
        
        int first = lst.get(0);
        int second = Integer.MAX_VALUE;
        
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < first) {
                second = first;
                first = lst.get(i);
            } else if (lst.get(i) < second && lst.get(i) != first) {
                second = lst.get(i);
            }
        }
        
        if (second == Integer.MAX_VALUE) {
            return Optional.empty();
        } else {
            return Optional.of(second);
        }
    }
}
```
This solution iterates through the list and keeps track of the smallest and second smallest elements. If the list has less than 2 elements, it returns an empty Optional. If the second smallest element is not found, it also returns an empty Optional. Otherwise, it returns an Optional containing the second smallest element.