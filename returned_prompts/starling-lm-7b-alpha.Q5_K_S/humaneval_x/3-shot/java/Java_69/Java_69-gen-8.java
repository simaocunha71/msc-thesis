        Map<Integer, Integer> frequency = new HashMap<>();
        for (int n : lst) {
            int value = frequency.getOrDefault(n, 0);
            frequency.put(n, value + 1);
        }
        for (int n : frequency.keySet()) {
            if (frequency.get(n) >= n) return n;
        }
        return -1;
    }
}

