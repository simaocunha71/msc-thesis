        Map<Integer, Integer> frequency_map = new HashMap<>();
        for (int i : lst) {
            frequency_map.put(i, frequency_map.getOrDefault(i, 0) + 1);
        }

        int max_freq = -1;
        for (int i : frequency_map.keySet()) {
            if (frequency_map.get(i) >= i && frequency_map.get(i) > max_freq) {
                max_freq = frequency_map.get(i);
            }
        }
        return max_freq;
    }
}

