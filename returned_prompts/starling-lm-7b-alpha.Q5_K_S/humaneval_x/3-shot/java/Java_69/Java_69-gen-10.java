        Map<Integer, Integer> freq_map = new HashMap<>();
        for (int n : lst) {
            int count = freq_map.getOrDefault(n, 0);
            freq_map.put(n, count + 1);
        }

        for (int key : freq_map.keySet()) {
            if (freq_map.get(key) >= key) return key;
        }
        return -1;
    }
}

