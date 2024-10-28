        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for  (int num : arr) {
            heap.offer(num);
            if  (heap.size() > k) {
                heap.poll();
            }
        }
        List<Integer> result = new ArrayList<>(heap);
        Collections.sort(result, Collections.reverseOrder());
        return result;
     }
}

