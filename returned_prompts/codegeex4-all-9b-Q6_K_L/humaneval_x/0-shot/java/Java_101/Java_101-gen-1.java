Here is the solution in Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> wordStrings(String s) {
        return Arrays.asList(s.replaceAll("[^a-zA-Z0-9]+", " ").split(" "));
    }
}
```

This solution works by first replacing all characters that are not letters or numbers with spaces. This is done using the `replaceAll` method with the regular expression `[^a-zA-Z0-9]+`. This regular expression matches any character that is not a letter or a number. After this, the string is split into words using the `split` method with the space character as the delimiter. This gives an array of words, which is then converted to a list using the `Arrays.asList` method.