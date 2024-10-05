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
        int len1 = 0;
        int len2 = 0;
        for (String s : lst1)
            len1 += s.length();
        for (String s : lst2)
            len2 += s.length();
        if (len1 > len2)
            return lst2;
        else if (len1 < len2)
            return lst1;
        else
            return lst1;
    }

    public static void main(String[] args) {
        List<String> lst1 = new ArrayList<>();
        lst1.add("4");
        List<String> lst2 = new ArrayList<>();
        lst2.add("1");
        lst2.add("2");
        lst2.add("3");
        lst2.add("4");
        lst2.add("5");
        lst1 = totalMatch(lst1, lst2);
        System.out.println(lst1);
    }
}
