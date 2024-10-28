import java.util.*;
import java.lang.*;

class Solution {
    /**
    You are given a list of integers.
    Write a function nextSmallest() that returns the 2nd smallest element of the list.
    Return null if there is no such element.
    <p>
    nextSmallest(Arrays.asList(1, 2, 3, 4, 5)) == Optional[2]
    nextSmallest(Arrays.asList(5, 1, 4, 3, 2)) == Optional[2]
    nextSmallest(Arrays.asList()) == Optional.empty
    nextSmallest(Arrays.asList(1, 1)) == Optional.empty
     */
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst.size() < 2) {
            return Optional.empty();
        }
        int min = lst.get(0);
        int secondMin = 0;
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < min) {
                secondMin = min;
                min = lst.get(i);
            }
            else if (lst.get(i) < secondMin && lst.get(i) != min) {
                secondMin = lst.get(i);
            }
        }
        return Optional.of(secondMin);
    }
}