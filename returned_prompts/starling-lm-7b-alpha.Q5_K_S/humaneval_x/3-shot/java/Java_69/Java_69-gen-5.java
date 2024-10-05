        Map<Integer, Integer> frequency_map = new HashMap<>();

        for (int i : lst) {
            frequency_map.put(i, frequency_map.getOrDefault(i, 0) + 1);
        }
        List<Integer> sorted_keys = new ArrayList<>(frequency_map.keySet());
        Collections.sort(sorted_keys);

        for (int key : sorted_keys) {
            if (frequency_map.get(key) >= key) {
                return key;
            }
        }
        return -1;
    }
}

