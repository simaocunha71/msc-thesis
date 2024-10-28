import java.util.*;
import java.lang.*;

class Solution {
    public List<String> totalMatch(List<String> lst1, List<String> lst2) {
        if(lst1.size() == 0 || lst2.size() == 0) {
            return new ArrayList<String>();
        }
        int total1 = 0;
        for(String s : lst1) {
            total1 += s.length();
        }
        int total2 = 0;
        for(String s : lst2) {
            total2 += s.length();
        }
        if(total1 < total2) {
            return lst1;
        }
        return lst2;
    }
}