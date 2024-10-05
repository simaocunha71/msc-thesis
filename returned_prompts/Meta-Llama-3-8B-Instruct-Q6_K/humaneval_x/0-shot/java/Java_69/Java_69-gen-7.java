    public int search(List<Integer> lst) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int num : lst) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }
        for (int num : map.keySet()) {
            if (num > 0 && map.get(num) >= num) {
                return num;
            }
        }
        return -1;
    }
}