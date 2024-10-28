        int max_count = -1;
        int max_value = -1;

        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i : lst) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() >= entry.getKey()) {
                max_count = Math.max(max_count, entry.getValue());
                max_value = entry.getKey();
            }
        }

        if (max_value == -1 || max_count < max_value) return -1;
        else return max_value;
    }
}

