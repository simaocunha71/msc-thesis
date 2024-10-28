    public int search(List<Integer> lst) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i : lst) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        int max = 0;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getKey() > 0 && entry.getValue() >= entry.getKey()) {
                max = Math.max(max, entry.getKey());
            }
        }
        return max > 0 ? max : -1;
    }  // Time complexity: O(n), where n is the size of the input list.
    // Space complexity: O(n), where n is the size of the input list.
}
