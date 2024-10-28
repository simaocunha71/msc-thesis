        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        maxHeap.addAll(arr);
        List<Integer> result = new ArrayList<>();
        for  (int i = 0; i < k; i++) {
            result.add(maxHeap.poll());
        }
        return result;
    }
}

