```java
import java.util.*;
import java.lang.*;

class Solution {
    public String concatenate(List<String> strings) {
        if (strings == null || strings.isEmpty()) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        for (String s : strings) {
            sb.append(s);
        }
        return sb.toString();
    }
}
```
This solution first checks if the input list is null or empty. If it is, an empty string is returned. Otherwise, a StringBuilder is used to concatenate the strings in the list. The resulting string is then returned.