        Map<Integer, Integer> freq = new HashMap<>();
        for (int i : lst) {
            freq.put(i, freq.getOrDefault(i, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            if (entry.getValue() >= entry.getKey()) {
                return entry.getKey();
            }
        }
        return -1;
    }
}

