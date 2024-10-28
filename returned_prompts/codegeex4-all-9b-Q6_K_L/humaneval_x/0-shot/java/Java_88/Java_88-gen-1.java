import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> sortArray(List<Integer> array) {
        if (array == null || array.size() <= 1) {
            return array;
        }

        int n = array.size();
        int sum = array.get(0) + array.get(n - 1);
        Collections.sort(array);

        if (sum % 2 == 0) {
            Collections.reverse(array);
        }

        return array;
    }
}