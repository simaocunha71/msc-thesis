Here is a Java method that takes a list of integers and an integer delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements:

```java
import java.util.*;

class Solution {
    public List<Integer> intersperse(List<Integer> numbers, int delimiter) {
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < numbers.size(); i++) {
            result.add(numbers.get(i));
            if (i < numbers.size() - 1) {
                result.add(delimiter);
            }
        }
        return result;
    }
}
```

You can use this method to intersperse a list of integers with a delimiter, like this:

```java
List<Integer> numbers = Arrays.asList(1, 2, 3);
int delimiter = 4;
List<Integer> result = new Solution().intersperse(numbers, delimiter);
System.out.println(result);  // [1, 4, 2, 4, 3]
```


The method iterates over the input list, adding each element to the result list. If the current index is not the last index of the list, it also adds the delimiter to the result list. This effectively inserts the delimiter between every two consecutive elements of the input list. The method returns the resulting list.

This solution has a time complexity of O(n), where n is the size of the input list, because it iterates over the list once. The space complexity is also O(n), because it creates a new list to store the result.