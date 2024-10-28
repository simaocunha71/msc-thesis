        List<Integer> result = new ArrayList<>();
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < arr.size(); i++) {
            if (i < k) {
                queue.add(arr.get(i));
            } else {
                if (arr.get(i) > queue.peek()) {
                    queue.remove();
                    queue.add(arr.get(i));
                }
            }
        }

        while (!queue.isEmpty()) {
            result.add(queue.remove());
        }

        return result;
    }
}

