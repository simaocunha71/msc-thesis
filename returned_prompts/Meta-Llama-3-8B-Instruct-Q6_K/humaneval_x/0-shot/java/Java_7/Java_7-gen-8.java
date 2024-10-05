Here is the Java code that filters a list of strings to only include those that contain a given substring:
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
Here's an explanation of the code:

*   We create an empty list `result` to store the filtered strings.
*   We iterate through the input list of strings `strings` using a foreach loop.
*   For each string `s`, we check if it contains the given substring `substring` using the `contains()` method.
*   If the string contains the substring, we add it to the `result` list.
*   Finally, we return the `result` list, which contains only the strings that contain the given substring.  🎉

You can test this method with the provided examples:
```java
List<String> strings = Arrays.asList("abc", "bacd", "cde", "array");
String substring = "a";
List<String> result = new Solution().filterBySubstring(strings, substring);
System.out.println(result);  // Output: [abc, bacd, array]
```
This code should produce the expected output for the given examples. Let me know if you have any further questions! 😊 