        String max = "";
        for (String word : words) {
            Set<Character> set = new HashSet<>();
            for (char c : word.toCharArray()) {
                set.add(c);
            }
            if (set.size() > max.length()) {
                max = word;
            } else if (set.size() == max.length()) {
                if (word.compareTo(max) < 0) {
                    max = word;
                }
            }
        }
        return max;
    }
}

