    public List<Integer> maximum(List<Integer> arr, int k) {
        // Create a priority queue and add all elements from the array
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for (int num : arr) {
            pq.offer(num);
        }

        // Create a list to store the maximum k numbers
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            result.add(pq.poll());
        }

        // Sort the result list in ascending order
        Collections.sort(result);

        return result;
    }
    B:
    public List<Integer> maximum(List<Integer> arr, int k) {
        // Create a list to store the maximum k numbers
        List<Integer> result = new ArrayList<>();
        // Sort the array in descending order
        Collections.sort(arr, (a, b) -> b - a);

        // Add the maximum k numbers to the result list
        for (int i = 0; i < k; i++) {
            result.add(arr.get(i));
        }

        return result;
    }
    C:
    public List<Integer> maximum(List<Integer> arr, int k) {
        // Create a list to store the maximum k numbers
        List<Integer> result = new ArrayList<>();
        // Create a priority queue and add the first k elements from the array
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for (int i = 0; i < k; i++) {
            pq.offer(arr.get(i));
        }

        // Add the remaining elements from the array to the priority queue
        for (int i = k; i < arr.size(); i++) {
            if (pq.peek() < arr.get(i)) {
                pq.poll();
                pq.offer(arr.get(i));
            }
        }

        // Add the maximum k numbers to the result list
        while (!pq.isEmpty()) {
            result.add(pq.poll());
        }

        return result;
    }
    D:
    public List<Integer> maximum(List<Integer> arr, int k) {
        // Create a list to store the maximum k numbers
        List<Integer> result = new ArrayList<>();
        // Create a heap and add the first k elements from the array
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> a - b);
        for (int i = 0; i < k