Here is a simple way to solve this problem using a HashSet in Java. HashSet in Java does not allow duplicate elements. So, we can add every character in the string to the HashSet and the size of the HashSet will give us the number of distinct characters in the string.
```java
import java.util.*;
import java.lang.*;

class Solution {
    public int countDistinctCharacters(String string) {
        Set<Character> distinctCharacters = new HashSet<>();
        for (char c : string.toCharArray()) {
            distinctCharacters.add(c);
        }
        return distinctCharacters.size();
    }
}
```
In this code, we are creating a HashSet named `distinctCharacters`. We then iterate over every character in the input string. For each character, we add it to the `distinctCharacters` HashSet. Since HashSet does not allow duplicate elements, if a character is already in the HashSet, it will not be added again. At the end, we return the size of the HashSet, which is the number of distinct characters in the string.