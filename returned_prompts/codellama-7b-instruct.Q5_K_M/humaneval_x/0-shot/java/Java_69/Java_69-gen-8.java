        int max = 0;
        for (Integer i : lst) {
            if (i > max) {
                max = i;
            }
        }
        if (max <= 0) {
            return -1;
        }
        Map<Integer, Integer> map = new HashMap<>();
        for (Integer i : lst) {
            if (i > max) {
                continue A;
            }
            int c = map.getOrDefault(i, 0);
            if (c >= i) {
                continue A;
            }
            map.put(i, c + 1);
        }
        for (int i = max; i > 0; i--) {
            if (map.containsKey(i)) {
                return i;
            }
        }
        return -1;
    }
}
