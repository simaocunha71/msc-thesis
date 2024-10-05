import java.util.*;

class Solution {
    public Optional<Integer> nextSmallest(List<Integer> lst) {
        if (lst.size() < 2) return Optional.empty();
        // find the smallest element
        int smallest = lst.get(0);
        int smallestIndex = 0;
        for (int i = 1; i < lst.size(); i++) {
            if (lst.get(i) < smallest) {
                smallest = lst.get(i);
                smallestIndex = i;
            }
        }
        // find the next smallest element
        int nextSmallest = lst.get(smallestIndex + 1);
        for (int i = smallestIndex + 2; i < lst.size(); i++) {
            if (lst.get(i) < nextSmallest) {
                nextSmallest = lst.get(i);
            }
        }
        return Optional.of(nextSmallest);
    }
}
