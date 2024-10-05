        Map<String, Integer> result = new HashMap<>();
        String[] words = test.split(" ");
        for (String word : words) {
            if (!result.containsKey(word)) {
                result.put(word, 1);
            } else {
                result.put(word, result.get(word) + 1);
            }
        }
        int maxCount = 0;
        for (Map.Entry<String, Integer> entry : result.entrySet()) {
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue();
            }
        }
        Map<String, Integer> finalResult = new HashMap<>();
        for (Map.Entry<String, Integer> entry : result.entrySet()) {
            if (entry.getValue() == maxCount) {
                finalResult.put(entry.getKey(), entry.getValue());
            }
        }
        return finalResult;
    }
}

