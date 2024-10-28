        if(lst.size() < 2) return true;

        int prev = lst.get(0);
        boolean duplicates = false;

        for(int i = 1; i < lst.size(); i++) {
            if (lst.get(i) == prev) {
                if (duplicates) return false;
                duplicates = true;
            }
            if (lst.get(i) < prev) return false;
            prev = lst.get(i);
        }
        return true;
    }
}

*/

import java.util.*;
import java.lang.*;

class Solution  {
    public boolean isSorted(List<Integer> lst) {
        if(lst.size() < 2) return true;

        int prev = lst.get(0);
        boolean duplicates = false;

        for(int i = 1; i < lst.size(); i++) {
            if (lst.get(i) == prev) {
                if (duplicates) return false;
                duplicates = true;
            }
            if (lst.get(i) < prev) return false;
            prev = lst.get(i);
        }
        return true;
    }
}