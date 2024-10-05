        Map<String, Integer> result = new HashMap<>();
        String[] words = test.split(" ");
        int max_count = 0;

        for (String word : words) {
            int current_count = 0;
            for (String other_word : words) {
                if (word.equals(other_word)) current_count += 1;
            }
            if (current_count > max_count) {
                result.clear();
                max_count = current_count;
            }
            if (current_count == max_count) result.put(word, max_count);
        }
        return result;
    }
}

