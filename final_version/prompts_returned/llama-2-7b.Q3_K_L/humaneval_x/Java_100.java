import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> makeAPile(3)
    [3, 5, 7]
     */
    public List<Integer> makeAPile(int n) {
        List<Integer> res = new ArrayList<>();
        for (int i = 2; i <= n; i++) {
            res.add((i - 1 % 2 == 0 ? Math.ceil(i / 2) : Math.floor(i / 2)));
        }
        return res;
    }
}