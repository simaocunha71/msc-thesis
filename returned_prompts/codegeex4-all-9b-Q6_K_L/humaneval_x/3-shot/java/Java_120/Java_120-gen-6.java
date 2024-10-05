        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (Integer x : arr) {
            heap.add(x);
        }
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            result.add(heap.poll());
        }
        return result;
    }
}

