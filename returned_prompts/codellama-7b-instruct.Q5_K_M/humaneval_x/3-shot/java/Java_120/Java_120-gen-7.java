        PriorityQueue<Integer> max_heap = new PriorityQueue<>(k, Collections.reverseOrder());
        List<Integer> result = new ArrayList<>();

        for (int a : arr) {
            if (max_heap.size() < k) {
                max_heap.add(a);
            } else if (a > max_heap.peek()) {
                max_heap.remove();
                max_heap.add(a);
            }
        }

        while (!max_heap.isEmpty()) {
            result.add(0, max_heap.remove());
        }
        return result;
    }
}

