import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic(Arrays.asList(1, 2, 4, 20))
    true
    >>> monotonic(Arrays.asList(1, 20, 4, 10))
    false
    >>> monotonic(Arrays.asList(4, 1, 0, -10))
    true
     */
    public boolean monotonic(List<Integer> l) {
        if (l == null || l.size() < 2) return true;
        Map<String, List<Integer>> map = new HashMap<>();
        Set<String> seen = new TreeSet();
        
        int n = l.size();
        for(int i=0;i<n-1;i++) {
            String key = Integer.toString(((i + 2) % n));
            List<Integer> curr = map.get(key);
            if (curr == null) {
                curr = new ArrayList<>();
                map.put(key, curr);
                seen.add(key);
            }
            
            int i1 = Integer.valueOf((i + 1) % n),
                    i2 = Integer.valueOf((i + 2) % n),
                    i3 = Integer.valueOf((i + 3) % n);
            if (i1 < i2 && i2 < i3 ) {//(i1 < i2) && (i2 < i3))
                curr.add(Integer.valueOf(i2)); //(i2 + 1 > i3)?: i2 + 1, true);
                //(i2 + 1 == i3 || ((i2 + 1) - Integer.valueOf((i - 1) % n)) >= (i3 - i2) >= 0)) {//(i3 - i2 > 1)?:true, (i3 - 1) < 0);
                break;
            } else if ((i + 1) % n == (i + 2) % n && (i + 2) % n == (i + 