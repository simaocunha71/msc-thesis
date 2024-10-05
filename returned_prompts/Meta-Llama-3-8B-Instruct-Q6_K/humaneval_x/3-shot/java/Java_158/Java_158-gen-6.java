        String result = "";
        int max_chars = 0;
        for (String word : words) {
            Set<Character> set = new HashSet<>();
            for (char c : word.toCharArray()) {
                set.add(c);
            }
            if (set.size() > max_chars) {
                max_chars = set.size();
                result = word;
            }
        }
        return result;
    }
}

