        Map<String, Integer> result = new HashMap<>();
        int max_count = 0;
        for (char c : test.toCharArray()) {
            int current_count = result.get(String.valueOf(c)) == null ? 0 : result.get(String.valueOf(c));
            result.put(String.valueOf(c), current_count + 1);
            max_count = Math.max(current_count + 1, max_count);
        }
        result.clear();
        for (String key : result.keySet()) {
            if (result.get(key) == max_count) {
                result.put(key, result.get(key));
            } else {
                result.remove(key);
            }
        }
        return result;
    }
}


