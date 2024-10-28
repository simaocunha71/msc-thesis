import java.util.*;

class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        int smallestEven = Integer.MAX_VALUE;
        int smallestEvenIndex = -1;

        for (int i = 0; i < arr.size(); i++) {
            int num = arr.get(i);
            if (num % 2 == 0 && num < smallestEven) {
                smallestEven = num;
                smallestEvenIndex = i;
            }
        }

        if (smallestEvenIndex == -1) {
            return new ArrayList<>();
        }

        return Arrays.asList(smallestEven, smallestEvenIndex);
    }
}