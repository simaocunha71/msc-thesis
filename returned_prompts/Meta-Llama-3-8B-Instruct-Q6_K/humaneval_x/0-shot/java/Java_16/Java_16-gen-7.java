    public int countDistinctCharacters(String string) {
        int count = 0;
        Set<Character> set = new HashSet<>();
        for (char c : string.toCharArray()) {
            set.add(Character.toLowerCase(c));
        }
        count = set.size();
        return count;
    } 
} 
