        Map<String, Integer> histogram = new HashMap<>();
        String[] words = test.split("\\s+");

        for (String word : words) {
            if (!histogram.containsKey(word)) {
                histogram.put(word, 1);
            } else {
                histogram.put(word, histogram.get(word) + 1);
            }
        }

        int maxCount = 0;
        List<String> maxWords = new ArrayList<>();

        for (Map.Entry<String, Integer> entry : histogram.entrySet()) {
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue();
                maxWords.clear();
                maxWords.add(entry.getKey());
            } else if (entry.getValue() == maxCount) {
                maxWords.add(entry.getKey());
            }
        }

        Map<String, Integer> result = new HashMap<>();

        for (String word : maxWords) {
            result.put(word, maxCount);
        }

        return result;
    }
}