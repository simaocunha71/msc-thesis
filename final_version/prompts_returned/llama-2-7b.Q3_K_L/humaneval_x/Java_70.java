import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strangeSortList(Arrays.asList(1, 2, 3, 4)) == Arrays.asList(1, 4, 2, 3)
    strangeSortList(Arrays.asList(5, 5, 5, 5)) == Arrays.asList(5, 5, 5, 5)
    strangeSortList(Arrays.asList()) == Arrays.asList()
     */
    public List<Integer> strangeSortList(List<Integer> lst) {
        if (lst == null || lst.size() < 1) return new ArrayList<Integer>(0);
        
        int min;
        int max = -1, i = -1;
        for (int num : lst) {
            while(++i < lst.size() && lst.get(i) <= num){
                //swap values
                List<Integer> temp = new ArrayList<>(lst);
                temp.set(max, num);
                min = i;
                max = --i;
                lst.set(min, lst.remove(max));
            }
        }
        
        Collections.reverse(lst);
        return lst;
    }
}