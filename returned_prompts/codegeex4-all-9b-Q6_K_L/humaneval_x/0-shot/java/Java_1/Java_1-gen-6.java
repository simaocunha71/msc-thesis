```java
import java.util.*;
import java.lang.*;

class Solution {
    public List<String> separateParenGroups(String paren_string) {
        // remove all spaces from the input string
        paren_string = paren_string.replaceAll(" ", "");

        // list to store the groups
        List<String> groups = new ArrayList<>();

        // variables to keep track of the current group
        String currentGroup = "";
        int openCount = 0;

        // iterate over each character in the string
        for (char c : paren_string.toCharArray()) {
            // if the character is an open parenthesis, increment the open count
            if (c == '(') {
                openCount++;
            } 
            // if the character is a closing parenthesis
            else if (c == ')') {
                openCount--;

                // if the open count is 0, we have completed a group
                if (openCount == 0) {
                    // add the current group to the list
                    groups.add(currentGroup);

                    // reset the current group
                    currentGroup = "";
                }
            }

            // add the character to the current group
            currentGroup += c;
        }

        return groups;
    }
}
```
