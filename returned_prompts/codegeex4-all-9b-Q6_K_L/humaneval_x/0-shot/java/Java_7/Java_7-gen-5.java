```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> filterBySubstring(List<String> strings, String substring) {
        if (strings == null || substring == null) {
            throw new IllegalArgumentException("Input list or substring cannot be null");
        }
        List<String> result = new ArrayList<>();
        for (String str : strings) {
            if (str.contains(substring)) {
                result.add(str);
            }
        }
        return result;
    }
}
```

This solution first checks if the input list or substring is null, and throws an IllegalArgumentException if it is. Then it iterates through the input list, checking if each string contains the given substring. If it does, it adds the string to the result list. Finally, it returns the result list.