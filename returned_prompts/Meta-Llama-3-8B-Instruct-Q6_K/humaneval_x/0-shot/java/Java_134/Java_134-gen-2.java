Here is the solution:
```java
import java.util.*;

class Solution {
    public boolean checkIfLastCharIsALetter(String txt) {
        if (txt.isEmpty()) return false;
        String[] words = txt.split("\\s+");
        if (words.length == 0) return false;
        String lastWord = words[words.length - 1];
        if (lastWord.isEmpty()) return false;
        char lastChar = lastWord.charAt(lastWord.length() - 1);
        return Character.isLetter(lastChar) && !Character.isLetter(lastWord.charAt(lastWord.length() - 2));
    }
}
```
This solution splits the input string into words using a regular expression that matches one or more whitespace characters (`\\s+`). It then checks if the last word is not empty. If it is not, it checks if the last character of the last word is a letter using the `Character.isLetter` method. It also checks if the character before the last character is not a letter using the same method. If both conditions are true, the method returns `true`; otherwise, it returns `false`. 

Note that this solution assumes that the input string does not contain any leading or trailing whitespace characters. If such characters are present, the solution would need to be modified to handle them. 

For example, the test case "apple pi e " would return `false` because the last character is a space. To handle this case, the solution could be modified to remove leading and trailing whitespace characters from the input string before processing it. 

Here is the modified solution:
```java
public boolean checkIfLastCharIsALetter(String txt) {
    txt = txt.trim();
    if (txt.isEmpty()) return false;
    String[] words = txt.split("\\s+");
    if (words.length == 0) return false;
    String lastWord = words[words.length - 1];
    if (lastWord.isEmpty()) return false;
    char lastChar = lastWord.charAt(lastWord.length() - 1);
    return Character.isLetter(lastChar) && !Character.isLetter(lastWord.charAt(lastWord.length() - 2));
}
```
This modified solution uses the `trim` method to remove leading and trailing whitespace characters from the input string before processing it. The rest of the solution remains the same. 

With this modification, the test case "apple pi e " would return `true` because the last character is an alphabetical character that is not part of a word. 