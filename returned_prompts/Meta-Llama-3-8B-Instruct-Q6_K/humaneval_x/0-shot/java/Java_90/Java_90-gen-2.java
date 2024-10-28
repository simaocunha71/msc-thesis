```java
import java.util.*;
import java.util.stream.*;

public class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst.isEmpty()) {
            return Optional.empty();
        }
        Optional<Integer> smallest = lst.stream().min(Comparator.naturalOrder());
        if (!smallest.isPresent()) {
            return Optional.empty();
        }
        int smallestValue = smallest.get();
        return lst.stream()
                .filter(x -> x != smallestValue)
                .min(Comparator.naturalOrder());
    }
}
```

Explanation:
This Java function `nextSmallest()` takes a list of integers as input and returns the 2nd smallest element if it exists, otherwise it returns an empty Optional. 

First, it checks if the list is empty. If it is, the function returns an empty Optional. 

Then, it finds the smallest element in the list using the `min()` method and a natural ordering comparator. If the list is empty or if all elements in the list are equal, the `min()` method will return an empty Optional.

Next, it filters out the smallest element from the list using the `filter()` method. 

Finally, it finds the smallest element in the filtered list using the `min()` method and a natural ordering comparator. This element is the 2nd smallest element in the original list. If the filtered list is empty (which means the original list had only one element), the `min()` method will return an empty Optional.

The function returns the 2nd smallest element as an Optional. If there is no 2nd smallest element (which means the list has less than two distinct elements), the function returns an empty Optional. 

This solution has a time complexity of O(n log n) due to the use of the `min()` method, where n is the size of the input list. The space complexity is O(n) due to the creation of a new stream for the filtered list. 

This solution uses Java 8's Stream API to simplify the code and make it more concise. It also uses Optional to handle the case where there is no 2nd smallest element. 

The unit tests provided in the problem statement ensure that the function works correctly for different input lists. 

The function is named `nextSmallest` to reflect its purpose of returning the next smallest element in the list. The function is public to allow it to be accessed from outside the class. The function takes a List of Integers as input and returns an Optional of Integer.