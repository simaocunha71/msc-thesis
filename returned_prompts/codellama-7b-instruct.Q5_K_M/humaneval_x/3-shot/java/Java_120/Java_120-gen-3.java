        PriorityQueue<Integer> max_heap = new PriorityQueue<>(k, Collections.reverseOrder());

        for (int i = 0; i < k; i++) {
            max_heap.add(arr.get(i));
        }

        for (int i = k; i < arr.size(); i++) {
            if (max_heap.peek() < arr.get(i)) {
                max_heap.poll();
                max_heap.add(arr.get(i));
            }
        }

        List<Integer> result = new ArrayList<>();
        while (!max_heap.isEmpty()) {
            result.add(max_heap.poll());
        }
        return result;
    }
}

