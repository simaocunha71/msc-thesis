    public int countDistinctCharacters(String string) {
        // Convert the string to lowercase
        string = string.toLowerCase();

        // Create a HashSet to store distinct characters
        Set<Character> set = new HashSet<>();

        // Iterate over the string and add each character to the set
        for (char c : string.toCharArray()) {
            set.add(c);
        }

        // Return the size of the set, which represents the number of distinct characters
        return set.size();
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.countDistinctCharacters("xyzXYZ")); // 3
        System.out.println(solution.countDistinctCharacters("Jerry")); // 4
    }
}