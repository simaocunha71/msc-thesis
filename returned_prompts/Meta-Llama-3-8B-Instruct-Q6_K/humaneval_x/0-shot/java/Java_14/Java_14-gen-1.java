Here is a Java solution that uses a loop to generate all prefixes of the input string and stores them in a List:

```java
import java.util.*;

class Solution {
    public List<String> allPrefixes(String string) {
        List<String> prefixes = new ArrayList<>();
        for (int i = 1; i <= string.length(); i++) {
            prefixes.add(string.substring(0, i));
        }
        return prefixes;
    }
}
```

This solution works by using a loop to iterate from 1 to the length of the input string. For each iteration, it uses the `substring` method to extract a substring from the beginning of the input string up to the current index `i`. This substring is then added to the `prefixes` List. Finally, the List is returned. The result is a List of all prefixes of the input string, in order from shortest to longest. For example, if the input string is "abc", the output would be ["a", "ab", "abc"].