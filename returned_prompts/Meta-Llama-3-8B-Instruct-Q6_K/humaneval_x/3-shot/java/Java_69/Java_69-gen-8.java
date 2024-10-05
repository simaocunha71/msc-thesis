        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : lst) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        int max = 0;
        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            if (entry.getKey() > 0 && entry.getValue() >= entry.getKey()) {
                max = Math.max(max, entry.getKey());
            }
        }
        return max > 0 ? max : -1;
    }
}

