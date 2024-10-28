import java.util.*;
import java.lang.*;

class Solution {
    /**
    Filter an input list of strings only for ones that contain given substring
    >>> filterBySubstring(List.of(), "a")
    []
    >>> filterBySubstring(Arrays.asList("abc", "bacd", "cde", "array"), "a")
    ["abc", "bacd", "array"]
     */
    public List<String> filterBySubstring(List<String> strings, String substring) {
        List<String> result = new ArrayList<>();
        for (String s : strings) {
            if (s.contains(substring)) {
                result.add(s);
            }
        }
        return result;
    }
}A: The problem is asking to create a method called `filterBySubstring` that takes a list of strings and a substring as parameters. This method should return a new list containing only the strings from the input list that contain the given substring.

Here is a simple solution using Java:

```java
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Filter an input list of strings only for ones that contain given substring
    >>> filterBySubstring(List.of(), "a")
    []
    >>> filterBySubstring(Arrays.asList("abc", "bacd", "cde", "array"), "a")
    ["abc", "bacd", "array"]
     */
    public List<String> filterBySubstring(List<String> strings, String substring) {
        List<String> result = new ArrayList<>();
        for (String s : strings) {
            if (s.contains(substring)) {
                result.add(s);
            }
        }
        return result;
    }
}
```

In this solution, we create an empty list `result` and iterate over each string `s` in the input list `strings`. We check if the string `s` contains the given substring using the `contains` method. If it does, we add the string `s` to the `result` list. Finally, we return the `result` list.

The time complexity of this solution is O(n*m) where n is the number of strings in the input list and m is the maximum length of a string in the input list. This is because in the worst case, we might have to iterate over each character of each string to check if it contains the substring. The space complexity is O(n) as we are storing the filtered strings in the `result` list.