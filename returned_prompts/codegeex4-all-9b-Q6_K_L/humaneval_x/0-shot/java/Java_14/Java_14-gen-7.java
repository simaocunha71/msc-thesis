```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> allPrefixes(String string) {
        List<String> result = new ArrayList<>();
        for (int i = 1; i <= string.length(); i++) {
            result.add(string.substring(0, i));
        }
        return result;
    }
}
```

Explanation: The function allPrefixes takes a string as input and returns a list of all prefixes from shortest to longest of the input string. The function uses a for loop to iterate through the length of the string and adds each prefix to the result list using the substring method. The substring method is used to get a substring of the input string from the start index to the end index. The start index is 0 and the end index is i, which represents the length of the current prefix. The result list is then returned.