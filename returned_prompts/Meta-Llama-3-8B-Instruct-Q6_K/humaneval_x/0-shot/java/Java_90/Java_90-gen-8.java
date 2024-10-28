```java
import java.util.*;

class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst.isEmpty() || lst.size() == 1) {
            return Optional.empty();
        }

        int min = lst.get(0);
        int secondMin = Integer.MAX_VALUE;

        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < min) {
                secondMin = min;
                min = lst.get(i);
            } else if (lst.get(i) < secondMin) {
                secondMin = lst.get(i);
            }
        }

        if (secondMin == Integer.MAX_VALUE) {
            return Optional.empty();
        }

        return Optional.of(secondMin);
    }
}
```

Explanation:
The function `nextSmallest` takes a list of integers as an input. It first checks if the list is empty or has only one element. If so, it returns an empty Optional. 

Then, it iterates through the list to find the smallest and the second smallest elements. It initializes `min` as the first element of the list and `secondMin` as the maximum possible integer value. 

In the loop, if it finds an element smaller than `min`, it updates `min` and `secondMin`. If it finds an element smaller than `secondMin` but not smaller than `min`, it updates `secondMin`. 

Finally, if `secondMin` is still the maximum possible integer value, it means there is no second smallest element, so it returns an empty Optional. Otherwise, it returns an Optional containing the second smallest element. 

This function has a time complexity of O(n), where n is the size of the input list, and a space complexity of O(1) as it only uses a constant amount of space. 