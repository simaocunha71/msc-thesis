        int n = grid.size();
        PriorityQueue<List<Integer>> pq = new PriorityQueue<>(k + 1, new Comparator<List<Integer>>() {
            public int compare(List<Integer> list1, List<Integer> list2) {
                for (int i = 0; i < list1.size(); i++) {
                    if (list1.get(i) != list2.get(i)) {
                        return list1.get(i) - list2.get(i);
                    }
                }
                return 0;
            }
        });

        pq.add(Arrays.asList(1));
        while (k-- > 0) {
            List<Integer> current = pq.poll();
            List<Integer> next = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                List<Integer> current_row = grid.get(i);
                for (int j = 0; j < n; j++) {
                    if (current.contains(current_row.get(j))) {
                        next.add(current_row.get(j));
                    }
                }
            }
            next.sort(Comparator.naturalOrder());
            pq.add(next);
        }
        return pq.poll();
    }
}

