        Map<Integer, Integer> frequency = new HashMap<>();
        int max = -1;

        for (int n : lst) {
            frequency.put(n, frequency.getOrDefault(n, 0) + 1);
            max = Math.max(max, frequency.get(n));
        }

        for (int n : frequency.keySet()) {
            if (frequency.get(n) >= n && n > max) {
                max = n;
            }
        }

        return max;
    }
}

