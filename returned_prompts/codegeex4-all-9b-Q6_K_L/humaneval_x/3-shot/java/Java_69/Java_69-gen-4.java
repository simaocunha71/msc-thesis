        Map<Integer, Integer> freq = new HashMap<>();

        for (int i : lst) {
            freq.put(i, freq.getOrDefault(i, 0) + 1);
        }

        int result = -1;

        for (int i : freq.keySet()) {
            if (freq.get(i) >= i && i > result) {
                result = i;
            }
        }
        return result;
    }
}

