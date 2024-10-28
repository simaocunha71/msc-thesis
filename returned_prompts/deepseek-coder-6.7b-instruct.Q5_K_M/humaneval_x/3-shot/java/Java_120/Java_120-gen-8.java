        PriorityQueue<Integer> heap = new PriorityQueue<>(k, Collections.reverseOrder());
        heap.addAll(arr);

        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            result.add(heap.poll());
        }
        return result;
    }
}

