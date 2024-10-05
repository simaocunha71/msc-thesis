import java.util.*;
import java.lang.*;

class Solution {
    public List<String> oddCount(List<String> lst) {
        ArrayList<String> output = new ArrayList<String>();
        for (int i=0; i<lst.size(); i++) {
            String s = lst.get(i);
            int oddCount = 0;
            for (int j=0; j<s.length(); j++) {
                if (s.charAt(j) % 2 == 1) {
                    oddCount++;
                }
            }
            output.add("the number of odd elements " + oddCount + "n the str" + oddCount + "ng " + oddCount + " of the " + oddCount + "nput.");
        }
        return output;
    }
}