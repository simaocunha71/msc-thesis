        List<Integer> res = new ArrayList<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>(k, new Comparator<Integer>() {
            public int compare(Integer o1, Integer o2) {
                return o2 - o1;
            }
        });

        for(int i = 0; i < arr.size() && k > 0; i++) {
            if (pq.size() < k) {
                pq.offer(arr.get(i));
            } else {
                int cur = pq.peek();
                if (arr.get(i) > cur) {
                    pq.poll();
                    pq.offer(arr.get(i));
                }
            }
        }

        while (!pq.isEmpty()) {
            res.add(0, pq.poll());
        }

        return res;
    }
}


