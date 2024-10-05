    public Map<String, Integer> histogram(String test) {
        Map<String, Integer> result = new HashMap<>();
        if (test.isEmpty()) {
            return result;
        }

        String[] words = test.split(" ");
        Map<String, Integer> count = new HashMap<>();

        for (String word : words) {
            if (!count.containsKey(word)) {
                count.put(word, 1);
            } else {
                count.put(word, count.get(word) + 1);
            }
        }

        int maxCount = 0;
        for (Map.Entry<String, Integer> entry : count.entrySet()) {
            if (entry.getValue() > maxCount) {
                maxCount = entry.getValue();
            }
        }

        for (Map.Entry<String, Integer> entry : count.entrySet()) {
            if (entry.getValue() == maxCount) {
                result.put(entry.getKey(), entry.getValue());
            }
        }

        return result;
    }  // The code above is the solution to the problem described. It correctly calculates the histogram of a given string by counting the occurrences of each word and then returning the words with the maximum count. If there are multiple words with the same maximum count, all of them are returned. The method first splits the input string into an array of words, then counts the occurrences of each word in a HashMap, and finally iterates over the HashMap to find the maximum count and the corresponding words. The result is a Map where the keys are the words with the maximum count and the values are their counts. If the input string is empty, the method returns an empty Map.