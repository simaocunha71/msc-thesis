        Map<String, Integer> result = new HashMap<>();
        String[] words = test.split(" ");
        for (String word : words) {
            if (!result.containsKey(word)) {
                result.put(word, 1);
            } else {
                result.put(word, result.get(word) + 1);
            }
        }
        return result;
    }
}

