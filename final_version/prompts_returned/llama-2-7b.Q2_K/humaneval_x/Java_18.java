import java.util.*;
import java.lang.*;

class Solution {
    /**
    Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> howManyTimes("", "a")
    0
    >>> howManyTimes("aaa", "a")
    3
    >>> howManyTimes("aaaa", "aa")
    3
     */
    public int howManyTimes(String string, String substring) {
        if (string == null || substring == null) return 0;
        Map<String, Integer> map = new HashMap<>();
        for (int i=0; i<string.length(); i++)
            map.putIfAbsent(substring+i, 1);
        int res = 0;
        map.forEach((k, v)-> { if (!map.containsKey("." + k)) res += v; });
        return res;
    }
}
