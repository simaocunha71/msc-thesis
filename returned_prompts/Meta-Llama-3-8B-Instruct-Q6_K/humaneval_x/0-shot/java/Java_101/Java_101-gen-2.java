Here is the solution:
```java
import java.util.*;

public class Solution {
    public List<String> wordStrings(String s) {
        String[] words = s.split("[,\\s]+");
        List<String> result = new ArrayList<>();
        for (String word : words) {
            result.add(word.trim());
        }
        return result;
    }
}
```
Explanation:
The problem is asking to split a given string into words and return them as a list. The string can contain commas or spaces as separators. 

We use the `split` method of the `String` class to split the string into words. The regular expression `[\\s,]+` matches one or more occurrences of a space (`\\s`) or a comma (`,`). 

Then, we use a `for` loop to add each word to the `result` list. We also use the `trim` method to remove any leading or trailing spaces from each word.

Finally, we return the `result` list.

You can test this solution with the given examples:
```java
System.out.println(new Solution().wordStrings("Hi, my name is John"));
System.out.println(new Solution().wordStrings("One, two, three, four, five, six"));
```
This will output:
```
[Hi, my, name, is, John]
[One, two, three, four, five, six]
``` 