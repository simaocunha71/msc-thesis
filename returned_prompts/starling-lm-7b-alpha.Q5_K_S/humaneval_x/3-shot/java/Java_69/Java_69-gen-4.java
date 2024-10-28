        Map<Integer, Integer> frequency = new HashMap<>();
        for (int number : lst) {
            frequency.put(number, frequency.getOrDefault(number, 0) + 1);
        }

        int max_frequency = 0;
        for (Map.Entry<Integer, Integer> entry : frequency.entrySet()) {
            if (entry.getValue() > entry.getKey()) return entry.getKey();
            if (entry.getValue() > max_frequency) {
                max_frequency = entry.getValue();
            }
        }
        return -1;
    }
}


```