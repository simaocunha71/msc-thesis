import java.util.*;
import java.lang.*;

class Solution {
    public List<String> oddCount(List<String> lst) {
        List<String> out = new ArrayList<String>();
        for (String s : lst) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if (Character.isDigit(c) && Integer.parseInt(String.valueOf(c)) % 2 == 1) {
                    count++;
                }
            }
            out.add("the number of odd elements " + count + "n the str" + count + "ng " + count + " of the " + count + "nput.");
        }
        return out;
    }
}