        List<String> prefixes = new ArrayList<>();
        for (int i = 0; i < string.length(); i++) {
            prefixes.add(string.substring(0, i + 1));
        }
        return prefixes;
    }
}

Solution:
The solution is straightforward, we just need to iterate through the input string from the first character to the last, and for each iteration, we take the substring from the first character to the i-th character (inclusive) and add it to the prefixes list. In the end we return the prefixes list.

The time complexity of this solution is O(n^2) because for each character in the string we create a substring which is O(n). The space complexity is O(n) because we create a list of strings of size n.

Note: We use Java's `substring` method which is O(n) because it creates a new string that references the same characters in the original string.
*/

