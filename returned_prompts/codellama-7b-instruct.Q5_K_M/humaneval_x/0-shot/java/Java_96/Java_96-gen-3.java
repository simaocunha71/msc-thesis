import java.util.*;
import java.lang.*;

class Solution {
    /**
    Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    countUpTo(5) => [2,3]
    countUpTo(11) => [2,3,5,7]
    countUpTo(0) => []
    countUpTo(20) => [2,3,5,7,11,13,17,19]
    countUpTo(1) => []
    countUpTo(18) => [2,3,5,7,11,13,17]
     */
    public List<Integer> countUpTo(int n) {
        // write your code here
        List<Integer> list = new ArrayList<>();
        for (int i = 2; i < n; i++) {
            boolean flag = true;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                list.add(i);
            }
        }
        return list;
    }
}
