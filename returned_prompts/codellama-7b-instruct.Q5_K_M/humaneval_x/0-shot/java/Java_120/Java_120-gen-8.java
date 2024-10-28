        PriorityQueue<Integer> pq = new PriorityQueue<>(k, Collections.reverseOrder());

        for (int i = 0; i < k; i++) {
            pq.add(arr.get(i));
        }

        for (int i = k; i < arr.size(); i++) {
            if (arr.get(i) > pq.peek()) {
                pq.poll();
                pq.add(arr.get(i));
            }
        }

        List<Integer> ret = new ArrayList<>(k);

        while (!pq.isEmpty()) {
            ret.add(pq.poll());
        }

        return ret;
    }
}
