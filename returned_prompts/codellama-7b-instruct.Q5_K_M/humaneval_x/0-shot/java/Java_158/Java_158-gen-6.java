        String res = "";
        int max = 0;
        for (String word : words) {
            Set<Character> set = new HashSet<>();
            for (char c : word.toCharArray()) {
                set.add(c);
            }
            if (set.size() > max) {
                max = set.size();
                res = word;
            } else if (set.size() == max && res.compareTo(word) > 0) {
                res = word;
            }
        }
        return res;
    }
}
