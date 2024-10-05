        int maxFreq = -1;
        for (int i = 0; i < lst.size(); i++) {
            int x = lst.get(i);
            int freq = 1;
            for (int j = i + 1; j < lst.size(); j++) {
                if (lst.get(j) == x) {
                    freq++;
                } else {
                    break;
                }
            }
            if (freq >= x) {
                maxFreq = x;
                break;
            }
        }
        return maxFreq == -1 ? -1 : maxFreq;
    }
}


B:
import java.util.*;

class Solution {
    /**
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than
    zero, and has a frequency greater than or equal to the value of the integer itself.
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search(Arrays.asList(4, 1, 2, 2, 3, 1)) == 2
        search(Arrays.asList(1, 2, 2, 3, 3, 3, 4, 4, 4)) == 3
        search(Arrays.asList(5, 5, 4, 4, 4)) == -1
     */
    public int search(List<Integer> lst) {

        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : lst) {
            freq.put(x, freq.getOrDefault(x, 0) + 1);
        }
        for (int x = lst.get(0); x <= lst.get(lst.size() - 1); x++) {
            if (freq.get(x) >= x) {
                return x;
            }
        }
        return -1;
    }
}


C:
import java.util.*;

class Solution {
    /**
    You are given a non-empty