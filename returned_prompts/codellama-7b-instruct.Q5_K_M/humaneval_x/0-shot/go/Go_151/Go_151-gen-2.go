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
        // Write your solution here
        int first = lst.get(0);
        int second = lst.get(1);
        if (second < first) {
            return Optional.of(second);
        }
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < first) {
                second = first;
                first = lst.get(i);
            }
        }
        if (second == first) {
            return Optional.empty();
        }
        return Optional.of(second);
    }
}