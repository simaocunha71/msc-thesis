        List<String> prefixes = new ArrayList<>();
        for(int i = 1; i <= string.length(); i++) {
            prefixes.add(string.substring(0, i));
        }
        return prefixes;
    }
}

Explanation:
The function `allPrefixes` takes a string as input and returns a list of all prefixes of the string from shortest to longest.

The function iterates over the length of the input string, starting from 1 (since the empty string is considered a prefix). For each length `i`, it adds the substring of the input string from the beginning to `i` characters as a prefix to the list.

The list of prefixes is then returned. In the example provided, the input string is "abc", and the function returns the list `["a", "ab", "abc"]`. The function can handle strings of any length and returns all possible prefixes, including the empty string and the original string itself.