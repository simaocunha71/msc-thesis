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
        Set<String> maxWords = new HashSet<>();
        for (Map.Entry<String, Integer> entry : result.entrySet()) {
            if (entry.getValue() > max) {
                max = entry.getValue();
                maxWords.clear();
                maxWords.add(entry.getKey());
            } else if (entry.getValue() == max) {
                maxWords.add(entry.getKey());
            }
        }
        Map<String, Integer> finalResult = new HashMap<>();
        for (String word : maxWords) {
            finalResult.put(word, max);
        }
        return finalResult;
    }
}

