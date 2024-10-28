    Set<Character> distinctCharacters = new HashSet<>();
    for (char character : string.toCharArray()) {
        distinctCharacters.add(character);
    }

    return distinctCharacters.size();
    }
}








```
In this solution, we are using a HashSet to store the characters in the string and then returning the size of the HashSet, which represents the count of distinct characters in the string.

Here's a breakdown of the code:

1. We create a new HashSet called `distinctCharacters` to store the distinct characters from the string.
2. We iterate over each character in the string using a for-each loop.
3. For each character, we add it to the `distinctCharacters` HashSet using the `add()` method. This ensures that duplicate characters are not stored.
4. Finally, we return the size of the `distinctCharacters` HashSet, which represents the count of distinct characters in the string.

This solution has a time complexity of O(n), where n is the length of the string, as we are iterating over each character in the string once. The space complexity is O(k), where k is the number of distinct characters in the string, as we are storing all the distinct characters in the HashSet.

Overall, this solution provides an efficient way to count the number of distinct characters in a string.
```