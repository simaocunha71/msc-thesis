        Map<String, Integer> result = new HashMap<>();
        if (test.isEmpty()) return result;

        String[] words = test.split(" ");
        int max_count = 0;
        for (String word : words) {
            int count = result.getOrDefault(word, 0);
            result.put(word, count + 1);
            max_count = Math.max(max_count, count + 1);
        }

        Map<String, Integer> max_count_map = new HashMap<>();
        for (Map.Entry<String, Integer> entry : result.entrySet()) {
            if (entry.getValue() == max_count) {
                max_count_map.put(entry.getKey(), entry.getValue());
            }
        }
        return max_count_map;
    }
}

