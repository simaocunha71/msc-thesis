    public String findMax(List<String> words) {
        if (words == null || words.isEmpty()) {
            return "";
        }
        String result = words.get(0);
        int maxUniqueChars = 0;
        for (String word : words) {
            Set<Character> set = new HashSet<>();
            for (char c : word.toCharArray()) {
                set.add(c);
            }
            if (set.size() > maxUniqueChars) {
                maxUniqueChars = set.size();
                result = word;
            }
        }
        return result;
    }  // End of findMax function. 
}  // End of Solution class.