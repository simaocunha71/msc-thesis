        Map<String, Integer> result = new HashMap<>();
        int max_count = 0;
        for (char c : test.toCharArray()) {
            int count = result.getOrDefault(c + "", 0);
            count += 1;
            result.put(c + "", count);
            if (count > max_count) {
                max_count = count;
            }
        }
        return result;
    }
}

