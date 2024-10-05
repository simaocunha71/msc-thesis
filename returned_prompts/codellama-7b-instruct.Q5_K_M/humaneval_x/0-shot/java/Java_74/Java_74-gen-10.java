import java.util.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        List<String> list = new ArrayList<>();
        int count = 0;
        for (String s : lst1) {
            count += s.length();
        }
        int count2 = 0;
        for (String s : lst2) {
            count2 += s.length();
        }
        if (count2 <= count) {
            return lst2;
        }
        return lst1;
    }
}
