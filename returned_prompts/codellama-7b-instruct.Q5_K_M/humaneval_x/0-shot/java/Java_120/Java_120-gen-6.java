        int len = arr.size();
        PriorityQueue<Integer> heap = new PriorityQueue<>(k, Collections.reverseOrder());
        for (int i = 0; i < len; i++) {
            heap.offer(arr.get(i));
            if (heap.size() > k) {
                heap.poll();
            }
        }
        List<Integer> list = new ArrayList<>();
        while (!heap.isEmpty()) {
            list.add(0, heap.poll());
        }
        return list;
    }
}
