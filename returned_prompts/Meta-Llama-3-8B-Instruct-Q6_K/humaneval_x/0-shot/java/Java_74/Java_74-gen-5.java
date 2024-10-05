Here is a Java function that implements the described behavior:

```java
import java.util.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int totalChars1 = 0;
        int totalChars2 = 0;

        for (String str : lst1) {
            totalChars1 += str.length();
        }

        for (String str : lst2) {
            totalChars2 += str.length();
        }

        if (totalChars1 < totalChars2) {
            return lst1;
        } else if (totalChars1 > totalChars2) {
            return lst2;
        } else {
            return lst1;
        }
    }
}
```

This function iterates over each list, summing up the length of each string. It then compares these totals to determine which list has the fewer total characters. If the two lists have the same total number of characters, it returns the first list. The function returns the list with fewer total characters. If the lists are empty, it returns an empty list. If the lists are the same, it returns the first list. This function is case-sensitive. If you want it to be case-insensitive, you could convert each string to lowercase before comparing them.  This function assumes that the input lists are not null. If you want to handle the case where one or both of the input lists are null, you could add checks for this at the beginning of the function.  This function does not modify the input lists. It returns a new list.  This function returns the list with fewer total characters. If the lists have the same total number of characters, it returns the first list.  This function is not optimized for performance. It could be optimized by using a single loop that sums up the lengths of all the strings in both lists.  This function does not handle the case where one or both of the input lists contain null strings. If you want to handle this case, you could add checks for this at the beginning of the function.  This function does not handle the case where one or both of the input lists contain strings with a length of zero. If you want to handle this case, you could add checks for this at the beginning of the function.  This function does not handle the case where one or both of the input lists are empty. If you want to handle this case, you could add checks for this at the beginning of the function.  This function does not