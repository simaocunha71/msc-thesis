import java.util.*;
import java.lang.*;

class Solution {
    public List<List<Integer>> getRow(List<List<Integer>> lst, int x) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (lst == null || lst.size() == 0) {
            return res;
        }
        for (int i = 0; i < lst.size(); i++) {
            for (int j = 0; j < lst.get(i).size(); j++) {
                if (lst.get(i).get(j) == x) {
                    List<Integer> tmp = new ArrayList<Integer>();
                    tmp.add(i);
                    tmp.add(j);
                    res.add(tmp);
                }
            }
        }
        Collections.sort(res, new Comparator<List<Integer>>() {
            @Override
            public int compare(List<Integer> o1, List<Integer> o2) {
                if (o1.get(0) != o2.get(0)) {
                    return o1.get(0) - o2.get(0);
                } else {
                    return o2.get(1) - o1.get(1);
                }
            }
        });
        return res;
    }
}