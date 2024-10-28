        Map<String, Integer> letterCounts = new HashMap<String, Integer>();
        String[] words = test.split(" ");

        for (String word : words) {
            if (letterCounts.containsKey(word)) {
                letterCounts.put(word, letterCounts.get(word) + 1);
            } else {
                letterCounts.put(word, 1);
            }
        }

        int max = 0;
        for (Integer count : letterCounts.values()) {
            if (count > max) {
                max = count;
            }
        }

        Map<String, Integer> result = new HashMap<String, Integer>();
        for (String key : letterCounts.keySet()) {
            if (letterCounts.get(key) == max) {
                result.put(key, max);
            }
        }
        return result;
     }
}

