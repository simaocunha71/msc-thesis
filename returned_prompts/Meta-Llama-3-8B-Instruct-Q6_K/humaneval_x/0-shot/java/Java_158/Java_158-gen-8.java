    public String findMax(List<String> words) {
        String result = "";
        int maxCount = 0;
        for (String word : words) {
            Set<Character> set = new HashSet<>();
            for (char c : word.toCharArray()) {
                set.add(c);
            }
            if (set.size() > maxCount) {
                maxCount = set.size();
                result = word;
            } else if (set.size() == maxCount) {
                if (result.compareTo(word) > 0) {
                    result = word;
                }
            }
        }
        return result;
    }