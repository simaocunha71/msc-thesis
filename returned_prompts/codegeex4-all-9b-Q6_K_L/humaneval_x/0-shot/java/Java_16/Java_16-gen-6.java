public int countDistinctCharacters(String string) {
    // Use a set to store unique characters
    Set<Character> distinctChars = new HashSet<>();

    // Convert the string to lowercase and iterate through each character
    for (char c : string.toLowerCase().toCharArray()) {
        // Add each character to the set
        distinctChars.add(c);
    }

    // The size of the set is the number of distinct characters
    return distinctChars.size();
}