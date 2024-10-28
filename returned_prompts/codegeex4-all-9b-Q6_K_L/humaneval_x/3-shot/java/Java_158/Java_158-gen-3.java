        String max = "";
        int max_unique = 0;
        for (String word : words) {
            int unique = 0;
            Set<Character> unique_chars = new HashSet<>();
            for (char c : word.toCharArray()) {
                if (unique_chars.add(c)) unique += 1;
            }
            if (unique > max_unique) {
                max = word;
                max_unique = unique;
            }
        }
        return max;
    }
}

