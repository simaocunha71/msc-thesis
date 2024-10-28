    public int countDistinctCharacters(String string) {
        // convert string to lowercase
        string = string.toLowerCase();
        // create a set to store unique characters
        Set<Character> set = new HashSet<>();
        // iterate over the string and add characters to the set
        for (char c : string.toCharArray()) {
            set.add(c);
        }
        // return the size of the set, which represents the number of distinct characters
        return set.size();
    }
}  // This is the solution class where we define a method to count the distinct characters in a given string.

This class contains a method named `countDistinctCharacters` that takes a string as an input and returns the number of distinct characters in the string, regardless of the case. The method first converts the input string to lowercase using the `toLowerCase` method, then creates a `HashSet` to store unique characters. It then iterates over the characters in the string and adds each character to the set. Finally, it returns the size of the set, which represents the number of distinct characters in the string.

The time complexity of this solution is O(n), where n is the length of the input string, because it iterates over each character in the string once. The space complexity is also O(n), because in the worst case, all characters in the string are distinct, and the set will store all characters.  // This is the comment explaining the solution.  // This is the end of the solution.