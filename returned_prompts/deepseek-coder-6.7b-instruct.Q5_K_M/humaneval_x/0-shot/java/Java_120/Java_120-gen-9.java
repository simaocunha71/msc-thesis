        List<Integer> result = new ArrayList<>();
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        maxHeap.addAll(arr);
        
        for(int i = 0; i < k; i++){
            result.add(maxHeap.poll());
        }
        
       