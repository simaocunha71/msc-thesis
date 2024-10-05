        Map<Integer, Integer> freqs = new HashMap<>();
        int max = -1;

        for (int i : lst) {
            freqs.put(i, freqs.getOrDefault(i, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry : freqs.entrySet()) {
            if (entry.getKey() <= entry.getValue() && entry.getKey() > max) {
                max = entry.getKey();
            }
        }

        return max;
    }
}

