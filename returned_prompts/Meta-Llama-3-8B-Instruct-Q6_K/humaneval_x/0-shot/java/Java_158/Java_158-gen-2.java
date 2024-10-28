    public String findMax(List<String> words) {
        String max = "";
        int maxCount = 0;
        for (String word : words) {
            Set<Character> set = new HashSet<>();
            for (char c : word.toCharArray()) {
                set.add(c);
            }
            if (set.size() > maxCount) {
                max = word;
                maxCount = set.size();
            } else if (set.size() == maxCount) {
                if (word.compareTo(max) < 0) {
                    max = word;
                }
            }
        }
        return max;
    }  



