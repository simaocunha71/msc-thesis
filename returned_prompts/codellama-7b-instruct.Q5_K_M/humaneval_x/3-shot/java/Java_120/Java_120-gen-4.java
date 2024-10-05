        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);

        for (int i : arr) {
            if (pq.size() < k) {
                pq.add(i);
            } else if (i > pq.peek()) {
                pq.poll();
                pq.add(i);
            }
        }

        return new ArrayList<>(pq);
    }
}

