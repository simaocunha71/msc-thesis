        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for  (int num: arr) {
            queue.offer(num);
            if  (queue.size() > k) {
                queue.poll();
            }
        }

        List<Integer> result = new ArrayList<>();
        while  (!queue.isEmpty()) {
            result.add(queue.poll());
        }
        Collections.reverse(result);
        return result;
     }
}

