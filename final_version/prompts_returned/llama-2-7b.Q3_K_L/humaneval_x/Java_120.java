import java.util.*;
import java.lang.*;

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
        PriorityQueue<Pair<Integer, Integer>> pq = new PriorityQueue<>();
        HashMap<Integer,ArrayList<Integer>> map = new HashMap<>();
        
        for (int i = 0; i < arr.size(); i++) {
            ArrayList<Integer> list = map.get(arr.get(i));
            
            if (list == null) {
                list = new ArrayList<>();
                
                map.put(arr.get(i), list);
            }
            
            if (list.size() < k){
                pq.add(new Pair<>(arr.get(i), i));
                list.add(i, arr.get(i));
            } else {
                int i2 = Math.min(k - list.size(), i);
                
                for (int j = 0; j < i2; j++) {
                    list.set(j, list.get(j) + arr.get(i));
                }
            }
        }
        
        List<Integer> result = new ArrayList<>();
        