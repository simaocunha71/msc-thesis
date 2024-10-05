    public int search(List<Integer> lst) {
        Map<Integer, Integer> map = new HashMap<>();
        for (Integer i : lst) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        int max = -1;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getKey() > 0 && entry.getValue() >= entry.getKey()) {
                max = Math.max(max, entry.getKey());
            }
        }
        return max;
    }  // return -1 if no such value exist
}
