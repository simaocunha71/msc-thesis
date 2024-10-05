        Map<Integer, Integer> freq_map = new HashMap<>();
        for (int n : lst) {
            freq_map.put(n, freq_map.getOrDefault(n, 0) + 1);
        }

        for (int key : freq_map.keySet()) {
            if (freq_map.get(key) >= key) {
                return key;
            }
        }
        return -1;
    }
}

