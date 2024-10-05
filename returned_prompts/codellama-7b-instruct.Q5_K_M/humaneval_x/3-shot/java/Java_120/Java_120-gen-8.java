        PriorityQueue<Integer> pq = new PriorityQueue<>(k, Collections.reverseOrder());
        List<Integer> result = new ArrayList<>();

        for (int i = 0; i < arr.size(); i++) {
            if (pq.size() < k) {
                pq.offer(arr.get(i));
            } else {
                if (arr.get(i) > pq.peek()) {
                    pq.poll();
                    pq.offer(arr.get(i));
                }
            }
        }

        while (pq.size() != 0) {
            result.add(pq.poll());
        }

        return result;
    }
}

