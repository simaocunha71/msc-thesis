You can use a HashSet to store the distinct characters in the string. HashSet is a data structure that does not allow duplicate elements. You can convert the string to lowercase and then iterate through each character in the string. For each character, you can add it to the HashSet. Finally, you can return the size of the HashSet, which represents the number of distinct characters in the string.

Here is the updated code:

```java
import java.util.*;
import java.lang.*;

class Solution {
    public int countDistinctCharacters(String string) {
        Set<Character> distinctCharacters = new HashSet<>();
        string = string.toLowerCase();
        for (int i = 0; i < string.length(); i++) {
            distinctCharacters.add(string.charAt(i));
        }
        return distinctCharacters.size();
    }
}
```

This code will correctly count the number of distinct characters in the string, regardless of case.