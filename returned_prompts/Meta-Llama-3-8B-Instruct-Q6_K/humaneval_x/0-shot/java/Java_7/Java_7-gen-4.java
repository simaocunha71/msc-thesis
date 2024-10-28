```java
import java.util.*;

class Solution {
    public List<String> filterBySubstring(List<String> strings, String substring) {
        return strings.stream()
                .filter(s -> s.contains(substring))
                .collect(Collectors.toList());
    }
}
```
Explanation:
*   The problem is asking to filter a list of strings based on a given substring. 
*   We can use Java 8's Stream API to solve this problem. 
*   We first convert the list to a stream using `strings.stream()`. 
*   Then, we use the `filter` method to filter out the strings that do not contain the given substring. 
*   We use a lambda expression `s -> s.contains(substring)` to specify the condition for filtering. 
*   Finally, we collect the filtered stream into a list using `collect(Collectors.toList())`. 
*   The resulting list will contain only the strings that contain the given substring. 

Note: This solution uses Java 8's Stream API, which is not available in earlier versions of Java. If you are using an earlier version of Java, you can use a different approach, such as using a for loop to iterate over the list and add the matching strings to a new list. 

Example usage:
```java
List<String> strings = Arrays.asList("abc", "bacd", "cde", "array");
String substring = "a";
List<String> result = filterBySubstring(strings, substring);
System.out.println(result); // Output: [abc, bacd, array]
```  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ######  ###### 