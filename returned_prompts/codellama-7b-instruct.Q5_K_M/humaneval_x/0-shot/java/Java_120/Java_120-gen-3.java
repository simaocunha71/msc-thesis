        List<Integer> list = new ArrayList<>();
        for(int i = 0; i < k; i++) {
            int max = Integer.MIN_VALUE;
            int maxIndex = -1;
            for(int j = 0; j < arr.size(); j++) {
                if(arr.get(j) > max) {
                    max = arr.get(j);
                    maxIndex = j;
                }
            }
            list.add(max);
            arr.remove(maxIndex);
        }
        return list;
    }
}

class Solution {
    public List<Integer> maximum(List<Integer> arr, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i = 0; i < k; i++) {
            if(i < arr.size()) {
                pq.add(arr.get(i));
            }
        }
        for(int i = k; i < arr.size(); i++) {
            if(arr.get(i) > pq.peek()) {
                pq.poll();
                pq.add(arr.get(i));
            }
        }
        List<Integer> list = new ArrayList<>();
        while(!pq.isEmpty()) {
            list.add(pq.poll());
        }
        return list;
    }
}

class Solution {
    public List<Integer> maximum(List<Integer> arr, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(k, Collections.reverseOrder());
        for(int i = 0; i < k; i++) {
            pq.add(arr.get(i));
        }
        for(int i = k; i < arr.size(); i++) {
            if(arr.get(i) > pq.peek()) {
                pq.poll();
                pq.add(arr.get(i));
            }
        }
        List<Integer> list = new ArrayList<>();
        while(!pq.isEmpty()) {
            list.add(pq.poll());
        }