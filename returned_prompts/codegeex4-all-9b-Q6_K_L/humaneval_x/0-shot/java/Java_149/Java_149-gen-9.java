import java.util.*;
import java.lang.*;

class Solution {
    public List<String> listSort(List<String> lst) {
        // remove strings with odd lengths
        lst.removeIf(str -> str.length() % 2 != 0);
        // sort the list by length of each word, and then alphabetically
        lst.sort(Comparator.comparingInt(String::length).thenComparing(String::compareTo));
        return lst;
    }
}