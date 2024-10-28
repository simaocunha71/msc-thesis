        String[] words = test.split(" ");
        Map<String, Integer> countMap = new HashMap<String, Integer>();
        for (String word : words) {
            if (countMap.containsKey(word)) {
                countMap.put(word, countMap.get(word) + 1);
            } else {
                countMap.put(word, 1);
            }
        }

        int max = 0;
        for (Integer value : countMap.values()) {
            if (value > max) {
                max = value;
            }
        }

        Map<String, Integer> result = new HashMap<String, Integer>();
        for (Map.Entry<String, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() == max) {
                result.put(entry.getKey(), entry.getValue());
            }
        }

        return result;
    }
}

