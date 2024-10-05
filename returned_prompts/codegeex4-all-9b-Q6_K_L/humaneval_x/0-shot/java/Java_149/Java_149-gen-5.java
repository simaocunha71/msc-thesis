import java.util.*;
import java.lang.*;

class Solution {
    public List<String> listSort(List<String> lst) {

        List<String> result = new ArrayList<>();
        for (String str : lst) {
            if (str.length() % 2 == 0) {
                result.add(str);
            }
        }
        result.sort(Comparator.comparingInt(String::length).thenComparing(String::compareTo));
        return result;
    }
}