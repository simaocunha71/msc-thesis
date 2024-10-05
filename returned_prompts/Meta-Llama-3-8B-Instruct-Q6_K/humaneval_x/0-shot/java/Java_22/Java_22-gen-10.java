```java
import java.util.*;

public class Solution {
    public List<Integer> filterIntegers(List<Object> values) {
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
The problem is asking to filter a list of objects and return a new list containing only the integers. 

In the given Java solution, we iterate over the list of objects and check if each object is an instance of Integer. If it is, we add it to the result list. At the end, we return the result list.

The `instanceof` keyword is used to check if an object is an instance of a particular class or interface. In this case, we use it to check if the object is an instance of Integer. The `(Integer) value` cast is used to convert the object to an Integer, which is safe because we've already checked that it's an instance of Integer. 

This solution assumes that the input list may contain other types of objects besides Integer, and that we only want to keep the Integer values. It also assumes that the input list is not null, and that the Integer values in the list are valid (i.e. not null). If these assumptions are not valid, additional error checking may be necessary. 