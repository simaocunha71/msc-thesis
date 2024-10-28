Here is the solution in Java:

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

This solution iterates over the input list of strings and checks if each string contains the given substring using the `contains()` method. If a string contains the substring, it is added to the result list. Finally, the result list is returned.

The test cases you provided are also included:

```java
public static void main(String[] args) {
    Solution solution = new Solution();
    List<String> strings1 = new ArrayList<>();
    System.out.println(solution.filterBySubstring(strings1, "a")); // []

    List<String> strings2 = Arrays.asList("abc", "bacd", "cde", "array");
    System.out.println(solution.filterBySubstring(strings2, "a")); // ["abc", "bacd", "array"]
}
```

When you run this code, it will output:

```
[]
[abc, bacd, array]
```


This solution has a time complexity of O(n*m), where n is the number of strings in the input list and m is the average length of a string. This is because for each string, we are checking if it contains the substring, which takes O(m) time. The space complexity is O(n), as we are storing the filtered strings in a list.