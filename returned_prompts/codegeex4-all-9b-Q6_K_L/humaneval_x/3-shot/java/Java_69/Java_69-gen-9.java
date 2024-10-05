        Map<Integer, Integer> frequency = new HashMap<>();
        for (int n : lst) {
            frequency.put(n, frequency.getOrDefault(n, 0) + 1);
        }

        int max_freq = 0;
        for (int n : frequency.keySet()) {
            max_freq = Math.max(max_freq, frequency.get(n));
        }

        for (int n : frequency.keySet()) {
            if (frequency.get(n) >= n) return n;
        }

        return -1;
    }
}

