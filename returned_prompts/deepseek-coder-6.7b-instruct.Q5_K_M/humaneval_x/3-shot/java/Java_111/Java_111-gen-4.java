        String[] words = test.split(" ");
        Map<String, Integer> result = new HashMap<>();

        for (String word : words) {
            if (result.containsKey(word)) {
                result.put(word, result.get(word) + 1);
            } else {
                result.put(word, 1);
            }
        }

        int max = 0;
        for (Integer value : result.values()) {
            if (value > max) {
                max = value;
            }
        }

        Map<String, Integer> finalResult = new HashMap<>();
        for (Map.Entry<String, Integer> entry : result.entrySet()) {
            if (entry.getValue() == max) {
                finalResult.put(entry.getKey(), entry.getValue());
            }
        }
        return finalResult;
    }
}

