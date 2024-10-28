        List<Integer> result = new ArrayList<>();
        PriorityQueue<Integer> max_heap = new PriorityQueue<>(k, Collections.reverseOrder());
        for (int i = 0; i < arr.size(); i++) {
            if (max_heap.size() < k) {
                max_heap.add(arr.get(i));
            } else if (max_heap.peek() < arr.get(i)) {
                max_heap.poll();
                max_heap.add(arr.get(i));
            }
        }
        while (!max_heap.isEmpty()) {
            result.add(0, max_heap.poll());
        }
        return result;
    }
}

