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

This Java solution uses a for-each loop to iterate over the input list of objects. For each object, it checks if the object is an instance of the Integer class using the `instanceof` operator. If it is, the object is added to the result list. Finally, the result list is returned.

The `instanceof` operator is used to check if the object is an instance of the Integer class. This is because the problem statement asks to filter out any values that are not integers. The `instanceof` operator returns `true` if the object is an instance of the specified class, and `false` otherwise.

The `add` method is used to add the integer object to the result list. The `ArrayList` class is used to create the result list, which is a resizable array that can grow or shrink dynamically.

The `Map.of()` and `List.of()` methods are used to create immutable maps and lists, respectively. These methods are used to create a map or list with a fixed number of elements, and they are not modified after creation. In this case, they are used to provide additional test data for the filterIntergers method.