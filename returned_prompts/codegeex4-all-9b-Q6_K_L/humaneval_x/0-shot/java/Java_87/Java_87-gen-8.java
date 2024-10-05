import java.util.*;
import java.lang.*;

class Solution {
    public List<List<Integer>> getRow(List<List<Integer>> lst, int x) {
        List<List<Integer>> res = new ArrayList<>();
        if (lst == null || lst.size() == 0) {
            return res;
        }
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    res.add(Arrays.asList(i, j));
                }
            }
        }
        return res;
    }
}