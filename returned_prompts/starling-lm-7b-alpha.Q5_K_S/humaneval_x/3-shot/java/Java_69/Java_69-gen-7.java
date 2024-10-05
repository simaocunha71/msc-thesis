        Map<Integer, Integer> freq_map = new HashMap<>();
        for (int i : lst) {
            freq_map.merge(i, 1, Integer::sum);
        }
        for (int key : freq_map.keySet()) {
            if (freq_map.get(key) >= key) {
                return key;
            }
        }
        return -1;
    }
}

