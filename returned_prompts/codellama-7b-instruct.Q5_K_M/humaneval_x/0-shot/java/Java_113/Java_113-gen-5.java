import java.util.*;

class Solution {
    public List<String> oddCount(List<String> lst) {
        List<String> result = new ArrayList<String>();
        for (String s : lst) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if ((int) c % 2 == 1) {
                    count++;
                }
            }
            result.add("the number of odd elements " + count + "n the str" + count + "ng " + (count % 10) + " of the " + count + "nput.");
        }
        return result;
    }
}

