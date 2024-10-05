Here is a Java solution for the problem:

```java
import java.util.*;

class Solution {
    public Object splitWords(String txt) {
        String[] words = txt.split("\\s+");
        if(words.length == 0) {
            return txt.replace(",", "").toLowerCase().chars().filter(c -> 'a' <= c && c <= 'z').filter(c -> (c - 'a') % 2 == 1).count();
        }
        return Arrays.asList(words);
    }
}
```

In this solution, we first split the input string into words using the `split` method with a regular expression that matches one or more whitespace characters. If the resulting array is empty, it means that there were no whitespace characters in the input string, so we split the string on commas instead. We then convert the string to lowercase and count the number of characters that are lowercase letters with odd order in the alphabet. If the resulting array is not empty, we simply return it as a list of words.  The time complexity of this solution is O(n), where n is the length of the input string. The space complexity is also O(n), as we need to store the resulting list of words.  The `split` method has a time complexity of O(n), where n is the length of the input string, and the `replace` method has a time complexity of O(n), where n is the length of the input string. The `chars` method has a time complexity of O(n), where n is the length of the input string, and the `filter` method has a time complexity of O(n), where n is the length of the input string. The `count` method has a time complexity of O(n), where n is the length of the input string. Therefore, the overall time complexity of this solution is O(n).  The space complexity is O(n), as we need to store the resulting list of words.  The `split` method has a space complexity of O(n), where n is the length of the input string, and the `replace` method has a space complexity of O(n), where n is the length of the input string. The `chars` method has a space complexity of O(n), where n is the length of the input string, and the `filter` method has a space complexity of O(n), where n is the length of the input string. The `count` method has a space complexity of O(1), as it only returns an integer. Therefore, the