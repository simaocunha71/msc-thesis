```java
import java.util.*;
import java.lang.*;

class Solution {
    public Optional<String> longest(List<String> strings) {
        if(strings.isEmpty()) {
            return Optional.empty();
        }
        String max = strings.get(0);
        for(String s : strings) {
            if(s.length() > max.length()) {
                max = s;
            }
        }
        return Optional.of(max);
    }
}
```