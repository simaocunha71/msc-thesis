    import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> removeDuplicates(List<Integer> numbers) {
        return numbers.stream()
                .distinct()
                .collect(Collectors.toList());
    }
}

Explanation:
The problem is asking to remove all elements from the list that occur more than once. The order of elements should remain the same as in the input. 

We can solve this problem by using the Stream API in Java. The `distinct` function will remove all duplicate elements from the stream. We then collect the stream into a list using the `collect` function. 

Here's the code:

```java
public List<Integer> removeDuplicates(List<Integer> numbers) {
    return numbers.stream()
            .distinct()
            .collect(Collectors.toList());
}
```

This code will return a new list with all duplicate elements removed, preserving the original order. 

For example, if we call `removeDuplicates(Arrays.asList(1, 2, 3, 2, 4))`, the function will return `[1, 3, 4]`. 

This solution has a time complexity of O(n), where n is the number of elements in the input list, because we're using the `distinct` function which has a time complexity of O(n). The space complexity is also O(n), because we're creating a new list to store the distinct elements. 

This solution is efficient and easy to understand, making it a good choice for this problem. 