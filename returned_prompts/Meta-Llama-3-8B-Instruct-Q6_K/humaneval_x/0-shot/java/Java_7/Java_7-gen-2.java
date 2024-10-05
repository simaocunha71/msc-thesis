Here is the solution:
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

*   We create an empty list `result` to store the filtered strings.
*   We iterate through the input list `strings` using a for-each loop.
*   For each string `s` in the list, we check if it contains the given `substring` using the `contains()` method.
*   If the string contains the substring, we add it to the `result` list.
*   Finally, we return the `result` list containing the filtered strings.  This solution works by iterating through the list and checking each string to see if it contains the given substring. If it does, it adds the string to the result list. At the end, it returns the result list. The unit tests provided show the expected behavior of this function. It filters out any strings that do not contain the substring "a" and returns the remaining strings.  For example, if the input list is ["abc", "bacd", "cde", "array"] and the substring is "a", it will return ["abc", "bacd", "array"] because these are the strings that contain the substring "a".  If the input list is empty or the substring is not found in any of the strings, it will return an empty list.  This function is case-sensitive, so if you want to make it case-insensitive, you can convert both the string and the substring to lower case or upper case before comparing.  For example: `if (s.toLowerCase().contains(substring.toLowerCase()))`.  This will make the function ignore the case of the characters when comparing.  You can also use `Pattern` and `Matcher` classes from the `java.util.regex` package to make the function case-insensitive.  For example: `if (Pattern.matches(".*" + Pattern.quote(substring) + ".*", s))`.  This will make the function use regular expressions to match the substring, which is case-insensitive.  You can also use `String.matches()` method to make the function case-insensitive.  For example: `if (s.matches(".*" + substring + ".*"))