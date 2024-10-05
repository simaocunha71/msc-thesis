```java
import java.util.*;

class Solution {
    public List<String> filterBySubstring(List<String> strings, String substring) {
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


Explanation:
The provided problem is asking to create a method that filters a list of strings based on a given substring. The method should return a new list containing only the strings from the input list that contain the given substring.

In the given Java code, we use a for-each loop to iterate over each string in the input list. For each string, we use the `contains()` method to check if it contains the given substring. If it does, we add the string to the result list.

Finally, we return the result list containing the filtered strings.

The code is written in a functional programming style, where we create a new list and add elements to it as we iterate over the input list, rather than modifying the original list. This is a good practice in Java, as it allows for more flexibility and maintainability.