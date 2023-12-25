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
        if(n==0){
            return Collections.emptyList();
        }else{
            List<Integer> list = new LinkedList<>();
            for (; n % 2 == 1 ; n--) {
                int count = 1;
                while (count < n || n%count==0);
                if (n%count==0){
                    break;
                }else{
                    list.add(count-1);
                }
            }
            return list;
        }
}