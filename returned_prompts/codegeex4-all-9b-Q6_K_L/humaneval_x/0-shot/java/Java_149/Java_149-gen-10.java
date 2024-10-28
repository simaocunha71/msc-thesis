import java.util.*;
import java.lang.*;

class Solution {
    public List<String> listSort(List<String> lst) {
        List<String> res = new ArrayList<>();
        for (String s : lst) {
            if (s.length() % 2 == 0) {
                res.add(s);
            }
        }
        Collections.sort(res, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1.length() == o2.length()) {
                    return o1.compareTo(o2);
                } else {
                    return o1.length() - o2.length();
                }
            }
        });
        return res;
    }
}