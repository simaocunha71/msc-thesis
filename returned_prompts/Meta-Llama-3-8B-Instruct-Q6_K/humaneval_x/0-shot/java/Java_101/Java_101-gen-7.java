Here is a simple Java solution that uses the `split()` method to split the string into words, and then converts the resulting array into a list:

```java
import java.util.*;

class Solution {
    public List<String> wordStrings(String s) {
        String[] words = s.split(",| ");
        List<String> result = new ArrayList<>();
        for (String word : words) {
            result.add(word.trim());
        }
        return result;
    }
}
```

In this solution, the `split()` method is used to split the string into words. The regular expression ",| " matches either a comma or a space, so the string is split into words regardless of whether they are separated by commas or spaces. The resulting array of words is then converted into a list, and any leading or trailing whitespace is removed from each word using the `trim()` method.

This solution assumes that the input string is well-formed and does not contain any other characters that might be considered as word separators. If the input string can contain other characters that should be considered as word separators, the regular expression used in the `split()` method would need to be modified accordingly. For example, if the input string can contain semicolons or tabs, the regular expression could be ",| |;|\t". If the input string can contain any Unicode word separator, the regular expression could be "[\\p{Zs},;\\t\r\n\f\v]+".