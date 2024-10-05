Here's how you can implement it in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> wordStrings(String s) {
        return Arrays.asList(s.replaceAll("[^a-zA-Z0-9]", " ").trim().split(" "));
    }
}
```

This solution first replaces all non-alphanumeric characters with spaces using `replaceAll`, then trims any leading or trailing spaces using `trim`, and finally splits the string into words using `split(" ")`. The words are returned as a list using `Arrays.asList`.