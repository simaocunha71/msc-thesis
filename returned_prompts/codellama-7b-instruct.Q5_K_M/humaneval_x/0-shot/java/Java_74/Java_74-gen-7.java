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
        if (lst1.size() == 0 && lst2.size() == 0)
            return new ArrayList<String>();
        if (lst1.size() == 0)
            return lst2;
        if (lst2.size() == 0)
            return lst1;

        int[] count1 = countChars(lst1);
        int[] count2 = countChars(lst2);

        int total1 = 0;
        int total2 = 0;

        for (int i = 0; i < 256; i++) {
            total1 += count1[i];
            total2 += count2[i];
        }

        if (total1 > total2)
            return lst1;
        if (total1 < total2)
            return lst2;

        return lst1;
    }

    private int[] countChars(List<String> lst) {
        int[] count = new int[25