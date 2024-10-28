import java.util.*;
import java.lang.*;

class Solution {
    public List<String> oddCount(List<String> lst) {
        List<String> result = new ArrayList<String>();
        for (int i = 0; i < lst.size(); i++) {
            String str = lst.get(i);
            int oddCount = 0;
            for (int j = 0; j < str.length(); j++) {
                if (Character.isDigit(str.charAt(j)) && Integer.parseInt(String.valueOf(str.charAt(j))) % 2 == 1) {
                    oddCount++;
                }
            }
            result.add("the number of odd elements " + oddCount + "n the str" + oddCount + "ng " + oddCount + " of the " + oddCount + "nput.");
        }
        return result;
    }
}