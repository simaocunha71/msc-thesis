Here is the Java code to solve the problem:

```java
import java.util.*;

class Solution {
    public List<Integer> parseMusic(String s) {
        List<Integer> result = new ArrayList<>();
        int beats = 0;
        for (char c : s.toCharArray()) {
            if (c == 'o') {
                beats += 4;
            } else if (c == '|') {
                beats /= 2;
            } else if (c == '.') {
                beats /= 4;
            }
            result.add(beats);
        }
        return result;
    }
}
```
This code defines a method `parseMusic` that takes a string of musical notes as input and returns a list of integers representing the number of beats each note lasts.

The method iterates over the input string character by character. If the character is 'o', it adds 4 to the `beats` variable, which represents the number of beats the current note lasts. If the character is '|', it divides `beats` by 2, which represents a half note. If the character is '.', it divides `beats` by 4, which represents a quarter note.

The `beats` variable is updated after each character and the updated value is added to the result list.

Finally, the method returns the result list. The time complexity of this method is O(n), where n is the length of the input string, as it iterates over the string once. The space complexity is O(n), as it uses a list to store the result. 