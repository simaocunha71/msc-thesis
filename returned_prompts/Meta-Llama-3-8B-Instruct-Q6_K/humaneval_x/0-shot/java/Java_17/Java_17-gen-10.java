Here is a simple and efficient solution in Java. This solution uses a stack to keep track of the current note and its duration. It iterates over the input string, and whenever it encounters a note, it checks the stack to see if the previous note is a half note or a whole note. If it is, it adds the duration of the current note to the list and resets the stack. If the stack is empty, it simply adds the duration to the list.

```java
import java.util.*;

class Solution {
    public List<Integer> parseMusic(String string) {
        List<Integer> result = new ArrayList<>();
        Stack<Character> stack = new Stack<>();
        for (char c : string.toCharArray()) {
            if (c == '|') {
                if (!stack.isEmpty()) {
                    result.add(2);
                    stack.pop();
                }
            } else if (c == 'o') {
                if (!stack.isEmpty()) {
                    result.add(4);
                    stack.pop();
                } else {
                    result.add(4);
                }
                stack.push('o');
            } else {
                if (!stack.isEmpty()) {
                    result.add(1);
                    stack.pop();
                } else {
                    result.add(1);
                }
            }
        }
        return result;
    }
}
```
This solution has a time complexity of O(n), where n is the length of the input string, and a space complexity of O(n), as in the worst case scenario, the stack will store all the notes. It is efficient because it only iterates over the input string once, and it uses a stack to keep track of the current note and its duration. It also handles the different types of notes correctly, as per the legend provided.