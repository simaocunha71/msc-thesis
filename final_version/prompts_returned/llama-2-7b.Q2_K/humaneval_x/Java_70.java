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
        if (lst == null || lst.isEmpty()) return Collections.emptyList();
         // sort elements of list in ascending order,
         int[] arr = new int[lst.size() + 1];
        for (int i = 0; i < lst.size(); i++) {
            Integer num = lst.get(i);
            if (num != null) {
                int pos = arr.length - i;
                if ((!pos) || (!arr[pos])) {
                    // put minimum at first and then maximum of remaining elements
                    arr[pos] = pos + 1 == lst.size() ? lst.get(lst.size()) : lst.get(pos + 1);
                } else if (num > arr[pos]) {
                    arr[pos++] = num;
                }
            }
        }
         List<Integer> result = new ArrayList<>();
         for (int i = 0; i < lst.size();) {
             int pos = i;
             while ((!pos || !(arr[pos])) && arr[++i] == -1);
            if (!pos || arr[--i]) {
              result.add(i != pos ? lst.get(i) : arr[pos]);
               i++;
            }
             else break;
         }return result;
    }
}
