        if (lst == null || lst.size() == 0)
            return lst;

        Collections.sort(lst);
        List<Integer> result = new ArrayList<>();
        int start = 0;
        int end = lst.size() - 1;
        while (start <= end) {
            result.add(lst.get(start++));
            if (start <= end)
                result.add(lst.get(end--));
        }
        return result;
    }

}

*/

import java.util.*;
import java.lang.*;

class Solution  {
    public List<Integer> strangeSortList(List<Integer> lst) {

        if (lst == null || lst.size() == 0)
            return lst;

        Collections.sort(lst);
        List<Integer> result = new ArrayList<>();
        int start = 0;
        int end = lst.size() - 1;
        while (start <= end) {
            result.add(lst.get(start++));
            if (start <= end)
                result.add(lst.get(end--));
        }
        return result;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.strangeSortList(Arrays.asList(1, 2, 3, 4)));
        System.out.println(sol.strangeSortList(Arrays.asList(5, 5, 5, 5)));
        System.out.println(sol.strangeSortList(Arrays.asList()));
    }
}

//Test Cases
/*
[1, 4, 2, 3]
[5, 5, 5, 5]
[]
*/

//Solution Explanation:
/*
The solution sorts the given list in ascending order. Then it constructs a new list in a strange order by alternately taking the smallest and largest remaining elements from the sorted list.
*/

/*
Time complexity: O(n log n) due to sorting.
