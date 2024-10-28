        Map<String, Integer> result = new HashMap<>();
        String[] words = test.split(" ");
        for (String word : words) {
            if (result.containsKey(word)) {
                result.put(word, result.get(word) + 1);
            } else {
                result.put(word, 1);
            }
        }
        int max = 0;
        for (Map.Entry<String, Integer> entry : result.entrySet()) {
            if (entry.getValue() > max) {
                max = entry.getValue();
            }
        }
        Map<String, Integer> maxCount = new HashMap<>();
        for (Map.Entry<String, Integer> entry : result.entrySet()) {
            if (entry.getValue() == max) {
                maxCount.put(entry.getKey(), entry.getValue());
            }
        }
        return maxCount;
    }
}

