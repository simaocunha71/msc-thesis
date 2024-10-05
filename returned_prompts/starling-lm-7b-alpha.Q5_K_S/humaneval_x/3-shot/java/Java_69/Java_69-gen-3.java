        Map<Integer, Integer> freq_map = new HashMap<>();
        for (int i : lst) {
            freq_map.put(i, freq_map.getOrDefault(i, 0) + 1);
        }
        int max_freq = Collections.max(freq_map.values());
        for (int i : freq_map.keySet()) {
            if (freq_map.get(i) >= i) {
                return i;
            }
        }
        return -1;
    }
}

