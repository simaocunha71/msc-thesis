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
        int min = Integer.MAX_VALUE;
        int minIndex = -1;
        for (int i = 0; i < lst.size(); i++) {
            int num = lst.get(i);
            if (num < min) {
                min = num;
                minIndex = i;
            }
        }
        return minIndex == -1 ? Optional.empty() : Optional.of(lst.get(minIndex + 1));
    }
}

B:
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
        int min = Integer.MAX_VALUE;
