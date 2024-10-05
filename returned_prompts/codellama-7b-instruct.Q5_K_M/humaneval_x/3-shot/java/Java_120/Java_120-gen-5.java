        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(k, Collections.reverseOrder());

        for (int i = 0; i < arr.size(); i++) {
            if (pq.size() < k) {
                pq.add(arr.get(i));
            } else if (pq.peek() < arr.get(i)) {
                pq.poll();
                pq.add(arr.get(i));
            }
        }

        return new ArrayList<Integer>(pq);
    }
}

