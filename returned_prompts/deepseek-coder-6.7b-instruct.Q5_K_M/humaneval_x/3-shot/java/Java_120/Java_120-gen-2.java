        PriorityQueue<Integer> queue = new PriorityQueue<>(k, Collections.reverseOrder());
        queue.addAll(arr.subList(0, k));

        for (int i = k; i < arr.size(); i++) {
            if (arr.get(i) > queue.peek()) {
                queue.poll();
                queue.offer(arr.get(i));
            }
        }

        return new ArrayList<>(queue);
     }
}

