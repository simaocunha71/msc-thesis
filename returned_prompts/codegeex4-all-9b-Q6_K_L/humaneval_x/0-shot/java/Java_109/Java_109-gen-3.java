import java.util.*;
import java.lang.*;

class Solution {
    public boolean moveOneBall(List<Integer> arr) {
        if (arr.size() <= 1) {
            return true;
        }

        int minIndex = 0;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) < arr.get(minIndex)) {
                minIndex = i;
            }
        }

        if (minIndex == arr.size() - 1) {
            return true;
        }

        for (int i = minIndex + 1; i < arr.size(); i++) {
            if (arr.get(i) < arr.get(i - 1)) {
                return false;
            }
        }

        return true;
    }
}
