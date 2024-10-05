    public int search(List<Integer> lst) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : lst) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        int max = 0;
        for (int key : map.keySet()) {
            if (key > 0 && map.get(key) >= key) {
                max = Math.max(max, key);
            }
        }
        return max > 0 ? max : -1;
    }
}
