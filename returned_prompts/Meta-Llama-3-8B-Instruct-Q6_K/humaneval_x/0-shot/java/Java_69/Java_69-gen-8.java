    int max = -1;
    Map<Integer, Integer> map = new HashMap<>();
    for (int num : lst) {
        map.put(num, map.getOrDefault(num, 0) + 1);
    }
    for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
        if (entry.getKey() > 0 && entry.getValue() >= entry.getKey()) {
            max = Math.max(max, entry.getKey());
        }
    }
    return max;
}

