    List<String> prefixes = new ArrayList<>();
    for(int i = 1; i <= string.length(); i++) {
        prefixes.add(string.substring(0, i));
    }
    return prefixes;
}

Explanation:
The function `allPrefixes` takes a string as input and returns a list of all its prefixes from shortest to longest. It does this by iterating over the string and adding each prefix to the list. The prefix is obtained by calling the `substring` method on the string, passing the start index (0) and the end index (the current iteration number) as arguments. The list of all prefixes is then returned.

For example, if the input string is "abc", the function will return the list ["a", "ab", "abc"]. The prefix "a" is obtained by taking the first character of the string, the prefix "ab" is obtained by taking the first two characters of the string, and the prefix "abc" is obtained by taking the first three characters of the string.

This solution has a time complexity of O(n), where n is the length of the input string, because it iterates over the string once. It has a space complexity of O(n) as well, because it stores all prefixes in the list. 