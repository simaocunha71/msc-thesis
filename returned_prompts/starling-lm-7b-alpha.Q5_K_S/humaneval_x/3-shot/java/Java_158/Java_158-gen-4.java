        int max_len = 0;
        String result = "";
        for (String word : words) {
            Set<Character> set = new HashSet<>();
            for (char c : word.toCharArray()) {
                set.add(c);
            }
            if (set.size() > max_len) {
                max_len = set.size();
                result = word;
            } else if (set.size() == max_len && word.compareTo(result) < 0) {
                max_len = set.size();
                result = word;
            }
        }
        return result;
    }
}

