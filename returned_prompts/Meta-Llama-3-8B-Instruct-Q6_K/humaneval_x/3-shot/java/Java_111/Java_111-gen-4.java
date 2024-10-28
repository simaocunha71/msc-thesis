        Map<String, Integer> result = new HashMap<>();
        String[] letters = test.split("\\s+");

        for (String letter : letters) {
            if (result.containsKey(letter)) {
                result.put(letter, result.get(letter) + 1);
            } else {
                result.put(letter, 1);
            }
        }

        int max_count = 0;
        List<String> max_letters = new ArrayList<>();

        for (Map.Entry<String, Integer> entry : result.entrySet()) {
            if (entry.getValue() > max_count) {
                max_count = entry.getValue();
                max_letters.clear();
                max_letters.add(entry.getKey());
            } else if (entry.getValue() == max_count) {
                max_letters.add(entry.getKey());
            }
        }

        Map<String, Integer> final_result = new HashMap<>();

        for (String letter : max_letters) {
            final_result.put(letter, max_count);
        }

        return final_result;
    }
}

