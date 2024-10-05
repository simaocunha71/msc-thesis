Here is the solution for the problem:

```java
import java.util.*;

class Solution {
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

Explanation:
The problem is asking to create a function that filters a list of strings and returns a new list containing only the strings that contain a given substring. 

We can solve this problem by iterating over the input list of strings and checking if each string contains the given substring using the `contains()` method. If it does, we add it to the result list. Finally, we return the result list.

The unit tests provided ensure that the function works correctly for different inputs. For example, `filterBySubstring(List.of(), "a")` returns an empty list because the input list is empty. `filterBySubstring(Arrays.asList("abc", "bacd", "cde", "array"), "a")` returns a list containing "abc", "bacd", and "array" because they all contain the substring "a". 

The function is case-sensitive, so if you want to make it case-insensitive, you can convert both the string and the substring to lowercase or uppercase before comparing them. For example, `s.toLowerCase().contains(substring.toLowerCase())`. 