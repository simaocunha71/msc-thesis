Here is a Java solution using if-else conditions to check for the presence of whitespaces and commas, and then splitting the string accordingly.

```java
import java.util.*;

class Solution {
    public Object splitWords(String txt) {
        List<String> result = new ArrayList<>();
        String[] words = txt.split("\\s+");
        if (words.length > 0) {
            for (String word : words) {
                if (word.contains(",")) {
                    result.addAll(Arrays.asList(word.split(",")));
                } else {
                    result.add(word);
                }
            }
        } else {
            int count = 0;
            for (char c : txt.toLowerCase().toCharArray()) {
                if (c >= 'a' && c <= 'z' && (c - 'a') % 2 != 0) {
                    count++;
                }
            }
            return count;
        }
        return result;
    }
}
```

In the given solution, the `splitWords` method takes a string `txt` as input. It first splits the string into words using the `split` method with a regular expression that matches one or more whitespace characters (`\\s+`).

If the resulting array of words is not empty, the method then iterates over each word and checks if it contains a comma. If it does, it splits the word into individual words using the `split` method with a regular expression that matches a comma (`,`), and adds the resulting array of words to the `result` list.

If the word does not contain a comma, the method simply adds the word to the `result` list.

If the resulting array of words is empty, the method returns the count of lower-case letters with odd order in the alphabet. It does this by iterating over each character in the input string, converting it to lower case, and checking if it is a letter between 'a' and 'z' (inclusive). If it is, it checks if the letter's position in the alphabet is odd (i.e., `c - 'a'` is not divisible by 2). If it is, it increments a count variable.

Finally, the method returns the `result` list if it is not empty, or the count variable if it is.