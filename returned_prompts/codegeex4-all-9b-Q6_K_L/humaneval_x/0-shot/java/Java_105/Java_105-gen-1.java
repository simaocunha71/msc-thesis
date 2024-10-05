import java.util.*;
import java.lang.*;

class Solution {
    public List<String> byLength(List<Integer> arr) {
        List<Integer> filtered = new ArrayList<>();
        for (Integer x : arr) {
            if (x >= 1 && x <= 9) {
                filtered.add(x);
            }
        }
        List<String> result = new ArrayList<>();
        for (Integer x : filtered) {
            result.add(String.valueOf(x));
        }
        Collections.sort(result, new Comparator<String>() {
            public int compare(String a, String b) {
                return b.length() - a.length();
            }
        });
        return result;
    }
}