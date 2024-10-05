    import java.util.*;

class Solution {
    public List<Integer> pluck(List<Integer> arr) {
        if(arr.isEmpty()) return new ArrayList<>();

        int minEvenValue = Integer.MAX_VALUE;
        int minEvenIndex = -1;
        for(int i = 0; i < arr.size(); i++) {
            if(arr.get(i) % 2 == 0 && arr.get(i) < minEvenValue) {
                minEvenValue = arr.get(i);
                minEvenIndex = i;
            }
        }

        if(minEvenValue == Integer.MAX_VALUE) return new ArrayList<>();

        return new ArrayList<>(Collections.singletonList(new int[]{minEvenValue, minEvenIndex}));
    }
}

Explanation:

1. We first check if the array is empty, if it is, we return an empty list.
2. We initialize `minEvenValue` to `Integer.MAX_VALUE` and `minEvenIndex` to `-1`. 
   We will use `minEvenValue` to keep track of the smallest even value found so far, and 
   `minEvenIndex` to keep track of the index of this smallest even value.
3. We iterate over the array, for each element, we check if it is even and if its value is less than `minEvenValue`. 
   If it is, we update `minEvenValue` and `minEvenIndex` accordingly.
4. If `minEvenValue` is still `Integer.MAX_VALUE` after the loop, it means we didn't find any even values, so we return an empty list.
5. Otherwise, we return a list containing `minEvenValue` and `minEvenIndex`.

This solution has a time complexity of O(n) where n is the size of the input array. It has a space complexity of O(1) as we are using a constant amount of space. 