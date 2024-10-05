        String result = "";
        int max_length = 0;
        for (String word : words) {
            Set<Character> set = new HashSet<>();

            for (char c : word.toCharArray()) {
                set.add(c);
            }
            if (set.size() > max_length) {
                result = word;
                max_length = set.size();
            }
        }
        return result;
    }
}

