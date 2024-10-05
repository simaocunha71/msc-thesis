import java.util.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        int totalChars1 = 0;
        for (String s : lst1) {
            totalChars1 += s.length();
        }
        int totalChars2 = 0;
        for (String s : lst2) {
            totalChars2 += s.length();
        }
        if (totalChars1 < totalChars2) {
            return lst1;
        }
        if (totalChars2 < totalChars1) {
            return lst2;
        }
        return lst1;
    }
}
