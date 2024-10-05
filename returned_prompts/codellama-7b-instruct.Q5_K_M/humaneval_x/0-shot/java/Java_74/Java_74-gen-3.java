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
        int lst1TotalChars = 0;
        int lst2TotalChars = 0;
        for (String str : lst1) {
            lst1TotalChars += str.length();
        }
        for (String str : lst2) {
            lst2TotalChars += str.length();
        }
        if (lst1TotalChars == lst2TotalChars) {
            return lst1;
        } else if (lst1TotalChars > lst2TotalChars) {
            return lst2;
        } else {
            return lst1;
        }
    }
}

