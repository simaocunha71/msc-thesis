        List<Integer> sortedList = new ArrayList<Integer>();
        Collections.sort(lst);
        int i = 0;
        int j = lst.size() - 1;

        while(i <= j) {
            sortedList.add(lst.get(i));
            if(i != j)
                sortedList.add(lst.get(j));
            i++;
            j--;
        }
        return sortedList;
    }
}

This solution works by sorting the input list in ascending order, and then pairing the minimum and maximum values alternately from the sorted list, starting with the minimum value, and adding them to a new list. If there's an odd number of elements, the middle one will be added at the end.

This solution has a time complexity of O(n log n) due to the sorting operation, and a space complexity of O(n) for the new list.

Please note that the problem statement does not specify how to handle duplicate elements. The provided solution assumes that there can be duplicate elements in the input list.

Also, the problem statement does not specify what to do if the input list is null. The provided solution assumes that a null input list will be handled by returning an empty list.

I hope this helps, and let me know if you have any other questions.

*/

import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> strangeSortList(List<Integer> lst) {
        if (lst == null) return new ArrayList<>();
        List<Integer> sortedList = new ArrayList<Integer>();
        Collections.sort(lst);
        int i = 0;
        int j = lst.size() - 1;

        while(i <= j) {
            sortedList.add(lst.get(i));
            if(i != j)
                sortedList.add(lst.get(j));
            i++;
            j--;
        }
        return sortedList;
    }
}

// Test the solution
public class Main {
    public static void main(String[] args) {
        Solution s = new Solution();
