        int max_frequency = 0;
        int result = -1;
        Map<Integer, Integer> counts = new HashMap<>();
        for (Integer number : lst) {
            counts.put(number, counts.getOrDefault(number, 0) + 1);
        }
        for (int key : counts.keySet()) {
            if (counts.get(key) > key) {
                if (max_frequency < counts.get(key)) {
                    max_frequency = counts.get(key);
                    result = key;
                }
            }
        }
        return result;
    }
}

