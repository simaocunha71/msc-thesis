        List<Integer> list = new ArrayList<>();
        if (arr.size() == 0)
            return list;
        if (k == 0)
            return list;
        if (arr.size() < k)
            k = arr.size();
        list.add(arr.get(0));
        for (int i = 1; i < k; i++) {
            if (arr.get(i) > list.get(list.size() - 1)) {
                list.remove(list.size() - 1);
                list.add(arr.get(i));
            }
        }
        return list;
    }
}


B:
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> maximum(List<Integer> arr, int k) {
        if (arr == null || arr.size() == 0 || k == 0) {
            return new ArrayList<Integer>();
        }
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(k, Collections.reverseOrder());
        for (int i = 0; i < k && i < arr.size(); i++) {
            pq.offer(arr.get(i));
        }
        for (int i = k; i < arr.size(); i++) {
            if (arr.get(i) > pq.peek()) {
                pq.poll();
                pq.offer(arr.get(i));
            }
        }
        List<Integer> result = new ArrayList<Integer>();
        while (!pq.isEmpty()) {
            result.add(pq.poll());
        }
        return result;
    }
}


C:
import java.util.*;
import java.lang.*;

class Solution {
    public List<Integer> maximum(List<Integer> arr, int k) {
        if (arr == null || arr.size() == 0 || k == 0) {
            return new ArrayList<Integer>();
        }
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(k, Collections.reverseOrder());
        for (int