        String[] words = test.split(" ");
        Map<String, Integer> hist = new HashMap<>();

        for (String word : words) {
            hist.put(word, hist.getOrDefault(word, 0) + 1);
        }

        int max = 0;
        for (Integer count : hist.values()) {
            if (count > max) {
                max = count;
            }
        }

        Map<String, Integer> result = new HashMap<>();
        for (Map.Entry<String, Integer> entry : hist.entrySet()) {
            if (entry.getValue() == max) {
                result.put(entry.getKey(), entry.getValue());
            }
        }

        return result;
    }
}

