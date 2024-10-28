        List<Integer> result = new ArrayList<Integer>();
        int max = Integer.MIN_VALUE;
        int count = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) > max) {
                max = arr.get(i);
                count++;
            }
        }
        int num = 0;
        for (int i = 0; i < arr.size(); i++) {
            if (arr.get(i) == max) {
                num++;
                result.add(arr.get(i));
            }
            if (num == k) {
                break;
            }
        }
        return result;
    }
}


B:

import java.util.ArrayList;
import java.util.Collections;

class Solution {
    /**
    Given an array arr of integers and a positive integer k, return a sorted list
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
     */
    public List<Integer> maximum(List<Integer> arr, int k) {
        if (k > arr.size()) {
            return null;
        }
        // 排序
        Collections.sort(arr);
        // 取倒数第k个数
        return arr.subList(arr.size() - k,