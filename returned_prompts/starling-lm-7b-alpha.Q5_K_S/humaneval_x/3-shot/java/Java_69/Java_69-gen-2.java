        Map<Integer, Integer> freq = new HashMap<>();
        for (int i : lst) {
            freq.put(i, freq.getOrDefault(i, 0) + 1);
        }
        Integer max_freq = Collections.max(freq.values());
        for (int key : freq.keySet()) {
            if (freq.get(key) >= key) {
                return key;
            }
        }
        return -1;
    }
}

