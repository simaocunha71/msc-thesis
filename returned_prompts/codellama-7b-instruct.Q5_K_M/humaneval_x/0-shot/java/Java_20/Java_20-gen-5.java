import java.util.*;

class Solution {
    public List<Integer> findClosestElements(int[] arr, int k) {
        if (k > arr.length) {
            return new ArrayList<>();
        }
        int i = 0;
        int j = i + k - 1;
        while (j < arr.length - 1) {
            if (arr[j + 1] - arr[i] > arr[j] - arr[j - 1]) {
                i++;
            } else {
                j++;
            }
        }
        List<Integer> list = new ArrayList<>();
        for (int index = i; index <= j; index++) {
            list.add(arr[index]);
        }
        return list;
    }
}
