```java
import java.util.*;

class Solution {
    public List<Integer> filterIntergers(List<Object> values) {
        List<Integer> result = new ArrayList<>();
        for (Object value : values) {
            if (value instanceof Integer) {
                result.add((Integer) value);
            }
        }
        return result;
    }
}
```
Explanation:
The problem is asking to filter a list of objects and return a list of integers. We can use an instance of operator (`instanceof`) to check if an object is an instance of Integer class. If it is, we add it to the result list. If not, we ignore it.

The `instanceof` operator checks if the object is an instance of the specified class or any of its subclasses. In this case, we are checking if the object is an instance of `Integer` class. If it is, we know that it's an integer and we add it to the result list.

We iterate over the list of objects using a for-each loop and check each object using the `instanceof` operator. If the object is an instance of `Integer`, we add it to the result list. If not, we ignore it.

The `filterIntergers` method returns the list of integers that were found in the original list. If the original list is empty, the method returns an empty list. If the original list contains no integers, the method returns an empty list. If the original list contains one or more integers, the method returns a list containing those integers.