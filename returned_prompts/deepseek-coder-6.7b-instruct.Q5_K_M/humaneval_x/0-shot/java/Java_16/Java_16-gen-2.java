        Set<Character> distinctCharacters = new HashSet<Character>();
        for (int i = 0; i < string.length(); i++) {
            distinctCharacters.add(Character.toLowerCase(string.charAt(i)));
        }
        return distinctCharacters.size();
    }
}

The code works by creating a new HashSet, which is a collection that contains no duplicate elements. We then iterate over the input string, converting all characters to lowercase to ensure case-insensitivity.

The character is added to the HashSet, which automatically handles duplicates. Finally, the size of the HashSet is returned, which is the number of unique characters in the string.

This function is case-insensitive as it converts all characters to lowercase before adding them to the HashSet. It also counts spaces and punctuation as characters.

The time complexity of this function is O(n), where n is the length of the string. This is because we're iterating over the string once. The space complexity is also O(n), where n is the number of unique characters in the string. This is because in the worst case, every character in the string is unique, and we're storing each character in a HashSet.
