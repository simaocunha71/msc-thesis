        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> b - a);
        for (int i = 0; i < k; i++) {
            maxHeap.add(arr.get(i));
        }

        for (int i = k; i < arr.size(); i++) {
            if (maxHeap.peek() < arr.get(i)) {
                maxHeap.poll();
                maxHeap.add(arr.get(i));
            }
        }

        List<Integer> result = new ArrayList<>();
        while (!maxHeap.isEmpty()) {
            result.add(maxHeap.poll());
        }
        Collections.sort(result);
        Collections.reverse(result);
        return result;
    }
}

