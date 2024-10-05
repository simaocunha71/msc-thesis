import java.util.*;
import java.lang.*;

class Solution {
    public boolean moveOneBall(List<Integer> arr) {
        if (arr.size() == 0) {
            return true;
        }
        if (arr.size() == 1) {
            return true;
        }
        if (arr.size() == 2) {
            return arr.get(0) <= arr.get(1);
        }
        int[] arr1 = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            arr1[i] = arr.get(i);
        }
        Arrays.sort(arr1);
        int[] arr2 = new int[arr.size()];
        for (int i = 0; i < arr.size(); i++) {
            arr2[i] = arr.get(i);
        }
        for (int i = 0; i < arr.size(); i++) {
            if (arr1[i] != arr2[i]) {
                return false;
            }
        }
        return true;
    }
}
