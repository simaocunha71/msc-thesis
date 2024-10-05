        String result = null;
        int maxCount = 0;

        for (String word : words) {
            Set<Character> set = new HashSet<>();
            for (char c : word.toCharArray()) {
                set.add(c);
            }
            if (set.size() > maxCount) {
                maxCount = set.size();
                result = word;
            }
        }
        return result;
    }
}

