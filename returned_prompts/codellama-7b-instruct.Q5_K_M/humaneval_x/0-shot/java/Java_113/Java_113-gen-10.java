import java.util.*;

class Solution {
    public List<String> oddCount(List<String> lst) {
        List<String> result = new ArrayList<String>();
        for (String s : lst) {
            int count = 0;
            for (char c : s.toCharArray()) {
                if (Character.getNumericValue(c) % 2 == 1) {
                    count++;
                }
            }
            result.add("the number of odd elements " + count + "n the str" + count + "ng " + (result.size() + 1) + " of the " + (result.size() + 1) + "nput.");
        }
        return result;
    }
}