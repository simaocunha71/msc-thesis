        PriorityQueue<Integer> max_heap = new PriorityQueue<>((a, b) -> b - a);

        for (int element : arr) {
            if (max_heap.size() < k) {
                max_heap.add(element);
            } else if (element > max_heap.peek()) {
                max_heap.poll();
                max_heap.add(element);
            }
        }

        return new ArrayList<>(max_heap);
    }
}

