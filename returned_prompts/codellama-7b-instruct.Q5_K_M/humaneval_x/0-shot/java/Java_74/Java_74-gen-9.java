import java.util.*;
import java.lang.*;

class Solution {
    /**
    Write a function that accepts two lists of strings and returns the list that has
    total number of chars in the all strings of the list less than the other list.

    if the two lists have the same number of chars, return the first list.

    Examples
    totalMatch(Arrays.asList(), Arrays.asList()) -> []
    totalMatch(Arrays.asList("hi", "admin"), Arrays.asList("hI", "Hi")) -> ["hI", "Hi"]
    totalMatch(Arrays.asList("hi", "admin"), Arrays.asList("hi", "hi", "admin", "project")) -> ["hi", "admin"]
    totalMatch(Arrays.asList("hi", "admin"), Arrays.asList("hI", "hi", "hi")) -> ["hI", "hi", "hi"]
    totalMatch(Arrays.asList("4"), Arrays.asList("1", "2", "3", "4", "5")) -> ["4"]
     */
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {

        int totalChars1 = totalChars(lst1);
        int totalChars2 = totalChars(lst2);

        if (totalChars1 < totalChars2) {
            return lst1;
        } else if (totalChars1 > totalChars2) {
            return lst2;
        } else {
            return lst1;
        }
    }

    private int totalChars(List<String> lst) {
        int total = 0;
        for (String s : lst) {
            total += s.length();
        }
        return total;
    }
}
