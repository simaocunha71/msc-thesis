        PriorityQueue<Integer> max_heap = new PriorityQueue<>(k, Collections.reverseOrder());

        for (Integer num : arr) {
            if (max_heap.size() < k) {
                max_heap.add(num);
            } else if (num > max_heap.peek()) {
                max_heap.poll();
                max_heap.add(num);
            }
        }
        return new ArrayList<>(max_heap);
    }
}

