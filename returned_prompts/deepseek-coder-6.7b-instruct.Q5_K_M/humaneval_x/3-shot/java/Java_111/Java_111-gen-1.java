        String[] words = test.split(" ");
        Map<String, Integer> map = new HashMap<>();
        for (String word : words) {
            if (map.containsKey(word)) {
                map.put(word, map.get(word) + 1);
            } else {
                map.put(word, 1);
            }
        }

        // find the max occurrence
        int max = 0;
        for (Integer value : map.values()) {
            max = Math.max(max, value);
        }

        // filter out the keys with the max occurrence
        Map<String, Integer> result = new HashMap<>();
        for (String key : map.keySet()) {
            if (map.get(key) == max) {
                result.put(key, max);
            }
        }

        return result;
    }
}

