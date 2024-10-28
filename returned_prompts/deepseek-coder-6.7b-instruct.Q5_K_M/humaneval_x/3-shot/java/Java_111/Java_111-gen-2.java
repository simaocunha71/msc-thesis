        String[] words = test.split(" ");
        Map<String, Integer> counts = new HashMap<>();
        for (String word : words) {
            if (counts.containsKey(word)) {
                counts.put(word, counts.get(word) + 1);
            } else {
                counts.put(word, 1);
            }
        }

        // Find the maximum count
        int maxCount = 0;
        for (Integer count : counts.values()) {
            if (count > maxCount) {
                maxCount = count;
            }
        }

        // Filter the map to only include words with the maximum count
        Map<String, Integer> result = new HashMap<>();
        for (Map.Entry<String, Integer> entry : counts.entrySet()) {
            if (entry.getValue() == maxCount) {
                result.put(entry.getKey(), entry.getValue());
            }
        }

        return result;
    }
}

