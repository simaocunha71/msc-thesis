        int sum = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>(k, Collections.reverseOrder());

        for (int i = 0; i < k; i++) {
            heap.offer(arr.get(i));
        }

        for (int i = k; i < arr.size(); i++) {
            int old_value = heap.poll();
            heap.offer(old_value);
        }

        while (!heap.isEmpty()) {
            sum += heap.poll();
        }
        return sum;

    }
}

